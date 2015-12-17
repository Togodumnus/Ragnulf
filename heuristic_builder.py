import multiprocessing as mp
from threading import Thread
from sys import stdout, argv
import getopt
import time

from Cube import Cube

MAX_LENGTH   = 3 #taille max de la chaîne de mouvements par défaut
REFRESH_TIME = 1 #1sec refresh affichage procession
MOUVEMENTS = [
    "U", "Ui", "U2", "L", "Li", "L2",
    "F", "Fi", "F2", "R", "Ri", "R2",
    "B", "Bi", "B2", "D", "Di", "D2"
]

def readArgs():
    """
    readArgs

    Lecture des arguments passés au script, version avancée.
    En particulier, on veut lire --max=<taille max movements>

    :Returns:
        {Dict}
    """
    optlist, args = getopt.getopt(argv[1:], [], ['max='])
    return {k: v for k, v in optlist}

def watchProgress(count, max):
    """
    watchProgress

    Affiche la progression du process
    ie. count/max

    :Example:
        [===               ]  100 / 10000 combinaisons

    :Args:
        count   {multiprocessing.Value}
        max     {Number}
    """
    def printLine(p, a, b, state):
        stdout.write(
            "[" + "=" * p  +  " " * (30-p) + "] "
            + str(a) + "/" + str(b) + " combinaisons "
            + ('◦' if state & 1 else '•')
            + " \r"
        )
        stdout.flush()

    c = False
    while count.value < max:
        p = int(counter.value / max * 30)
        printLine(p, count.value, max, c)
        c = not c
        time.sleep(REFRESH_TIME)

    printLine(30, max, max, c)
    time.sleep(0.1)

def makeMove(queue, lock, counter, states, shortcuts, maximum):
    """
    makeMove

    Un worker. Consomme les tâches de `queue` et enregistre le résultat
    dans `states et `shortcuts`.

    `queue` représente une liste de rotation à effectuer sur le cube.
    Une action est de la forme (cube, history, longueur, mvt) où `mvt` est
    la rotation à effectuer sur `cube`.
    `historique` représente l'historique des mouvements faits sur ce cube, et
    `longueur` le nombre de rotation de l'historique.

    :Args:
        queue       {multiprocessing.manager.Queue}
        lock        {multiprocessing.Lock}
        counter     {multiprocessing.Value}
        states      {multiprocessing.manager.Dict}
        shortcuts   {multiprocessing.manager.Dict}
        maximum     {int}                           Taille max de la liste de
                                                    mouvements
    """

    while not queue.empty():

        #on récupère ce qu'on doit faire
        cube, history, longueur, mvt = queue.get()

        #on applique la rotation
        method = getattr(cube, 'rot_' + mvt)
        method()

        #l'état obtenu
        state = cube.to_line(colors=False)

        lock.acquire()
        if state in states: #si on a déjà rencontré l'état
            #on regarde quelle suite de mouvements amène à cet état
            mouvements, l = states[state]
            if longueur + 1 < l: #si notre solution actuelle est meilleure
                #on retient cette suite de mouvements pour arriver à cet état
                states[state] = history + mvt, longueur + 1
                #on ajoute un shortcut pour utiliser notre version plutôt que mouvements
                shortcuts[mouvements] = history + mvt
            elif longueur + 1 > l:
                #on ajoute un shortcut pour utiliser mouvements plutôt que notre version
                shortcuts[history + mvt] = mouvements
            #si égalité, on ne fait rien, car ne sert à rien de remplacer quoi que ce soit

        else: #sinon, nouvel état
            states[state] = history + mvt, longueur + 1

        counter.value += 1
        lock.release()

        queue.task_done() #tâche effectuée

        #si on n'atteint pas la limite de taille des mouvements à recherché,
        #on relance un niveau supplémentaire
        if longueur < maximum - 1:
            for m in MOUVEMENTS:
                #on ajoute à la queue
                queue.put((cube, history + mvt, longueur + 1, m))

    return


def logResultStates(states):
    for s, m in states:
        print(s + ' : ' + m[0]  + '(' + str(m[1]) + ')')

def logResultShortcuts(shortcuts):
    for m, s in shortcuts.items():
        print(m + ' --> ' + s)

def calcNbCombinaisons(q, max):
    """
    calcNbCombinaisons

    Calcule le nombre de combinaisions que l'on va traiter en fonction
    de la taille max de la liste de mouvements.

    C'est une somme de d'une suite géométrique:
        q + q^2 + ... q^MAX_LENGTH
        où q = 18 (le nombre de mouvements)

    :Args:
        q    {int}
        max  {int}
    """
    return int((1 - q**(max+1)) / (1 - q) - 1)

if __name__ == '__main__':

    args = readArgs()
    maximum = int(args['--max']) if '--max' in args else MAX_LENGTH

    start = time.time()

    cube = Cube() #un cube résolu

    with mp.Manager() as manager:

        """
        states

        Stocke la liste des état, et le plus court jeu de mouvements
        qui mènent à l'état

        {
            <state> : <list de mouvements>,
            YYYY......WWWW: ('U R ... ', <longueur mouvement>)
            ....
        }
        """
        states = manager.dict()
        #on remplit l'état inital
        states[cube.to_line(colors=False)] = ('ø', 0)

        """
        shortcuts

        {
            "U Ui" : '',
            ...
        }
        """
        shortcuts = manager.dict()

        counter = mp.Value('i', 0) #nombre de combinaisons traitées

        queue = manager.Queue()
        lock  = manager.Lock()

        #on commence à remplir queue avec les 18 premiers mouvements
        for m in MOUVEMENTS:
            queue.put((cube, '', 0, m))

        #on lance un watcher de progression
        watcher = Thread(
            target=watchProgress,
            args=(counter, calcNbCombinaisons(len(MOUVEMENTS), maximum)),
            daemon=True
        )
        watcher.start()

        #on crée un process par CPU pour distribuer autant que possible le
        #travail
        processes = [
            mp.Process(
                target=makeMove,
                args=(queue, lock, counter, states, shortcuts, maximum),
                daemon=True
            ) for i in range(mp.cpu_count())
        ]
        for proc in processes:
            proc.start()

        #on attend que la queue soit vide
        queue.join()
        #on attend watche aussi histoire de ne pas avoir de pb d'affichage
        watcher.join()

        for proc in processes:
            proc.terminate()

        listStates = sorted(states.items(), key=lambda l: l[1][1])
        logResultStates(listStates)

        logResultShortcuts(shortcuts)

        print(counter.value)

