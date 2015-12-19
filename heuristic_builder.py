from   threading import Thread
from   sys import stdout, argv
from   datetime import datetime, timedelta
import multiprocessing as mp
import getopt
import time
import json

from Cube import Cube

MAX_LENGTH   = 3 #taille max de la chaîne de mouvements par défaut
REFRESH_TIME = 1 #1sec refresh affichage procession
RATIO = 2        #ratio entre longueur suite de mouvements et longueur raccourci
MOUVEMENTS = [
    "U", "Ui", "U2", "L", "Li", "L2",
    "F", "Fi", "F2", "R", "Ri", "R2",
    "B", "Bi", "B2", "D", "Di", "D2"
]
SHORTCUTS_FILE = 'shortcuts.json'

def readArgs():
    """
    readArgs

    Lecture des arguments passés au script, version avancée.
    En particulier, on veut lire --max=<taille max movements>

    :Returns:
        {Dict}
    """
    optlist, args = getopt.getopt(argv[1:], [], [
        'output-file=',
        'max=',
        'ratio='
    ])
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

    INTERVAL = 30

    def printLine(p, a, b, start, end):
        #temps d'exécution
        t = (datetime.now().replace(microsecond=0) - start).total_seconds()
        #vitesse d'éxécution
        v = a / t if t > 0 else None
        #temps restant
        restant = str(timedelta(seconds=int((b-a) / v))) if v else '?'

        stdout.write(
            #représentation avancement
            "[" + "=" * p  +  " " * (30-p) + "] "
            #nombre done / nombre total
            + str(a) + "/" + str(b) + " combinaisons - "
            #évaluation temps restant
            + ' Remaining : ' + (restant) + 's'
            + (" \r" if not end else " \n")
        )
        stdout.flush()

    start = datetime.now().replace(microsecond=0) #date de début
    while count.value < max:
        p = int(counter.value / max * INTERVAL) #rapport d'avancement sur INTERVAL
        printLine(p, count.value, max, start, False) #afficher les infos
        time.sleep(REFRESH_TIME) #on attend

    #fin du travail, on affiche une dernière ligne
    printLine(INTERVAL, max, max, start, True)
    print('Done in', str(datetime.now().replace(microsecond=0) - start) + 's')
    time.sleep(0.1)

def makeMove(queue, lock, counter, states, shortcuts, ration, maximum):
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
        ratio       {float}                         Rapport minimal entre la
                                                    taille de suite de mouvements
                                                    et le raccourci
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

        if state in states: #si on a déjà rencontré l'état
            #on regarde quelle suite de mouvements amène à cet état
            mouvements, l = states[state]
            if longueur + 1 < l / ratio: #si notre solution actuelle est meilleure
                #on retient cette suite de mouvements pour arriver à cet état
                states[state] = history + mvt, longueur + 1
                #on ajoute un shortcut pour utiliser notre version plutôt que mouvements
                shortcuts[mouvements] = history + mvt
            elif longueur + 1 > l * ratio: #si la solution historique est meilleure
                #on ajoute un shortcut pour utiliser mouvements plutôt que notre version
                shortcuts[history + mvt] = mouvements
            #sinon, on ne fait rien, car ne sert à presque rien de remplacer quoi que ce soit

        else: #sinon, nouvel état
            states[state] = history + mvt, longueur + 1

        lock.acquire()
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

def saveResultShortcuts(shortcuts, file):
    """
    saveResultShortcuts

    :Args:
        shortcuts   {Dict}
        file        {String}
    """
    with open(file, 'w') as outfile:
        json.dump(shortcuts, outfile)

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
    maximum       = int(args['--max']) if '--max' in args else MAX_LENGTH
    shortcutsFile = args['--output-file'] if '--output-file' in args else SHORTCUTS_FILE
    ratio         = float(args['--ratio']) if '--ratio' in args else RATIO


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
        cpus = mp.cpu_count()
        processes = [
            mp.Process(
                target=makeMove,
                args=(queue, lock, counter, states, shortcuts, ratio, maximum),
                daemon=True
            ) for i in range(cpus - 1 if cpus > 1 else 1)
        ]
        for proc in processes:
            proc.start()

        #on attend que la queue soit vide
        queue.join()
        #on attend watche aussi histoire de ne pas avoir de pb d'affichage
        watcher.join()

        for proc in processes:
            proc.terminate()

        # listStates = sorted(states.items(), key=lambda l: l[1][1])

        saveResultShortcuts(dict(shortcuts), shortcutsFile)
        print('Output saved in', shortcutsFile)
