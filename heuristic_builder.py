import multiprocessing as mp

import time
from Cube import Cube

MAX_LENGTH = 3
MOUVEMENTS = [
    "U", "Ui", "U2", "L", "Li", "L2",
    "F", "Fi", "F2", "R", "Ri", "R2",
    "B", "Bi", "B2", "D", "Di", "D2"
]

def makeMove(queue, lock, counter, states, shortcuts):
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
        queue   {multiprocessing.manager.Queue}
        lock    {multiprocessing.Lock}
        counter {multiprocessing.Value}
        states  {multiprocessing.manager.Dict}
        shortcuts  {multiprocessing.manager.Dict}
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
        if longueur < MAX_LENGTH - 1:
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

if __name__ == '__main__':

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

        #on crée un process par CPU
        processes = [
            mp.Process(
                target=makeMove,
                args=(queue, lock, counter, states, shortcuts)
            ) for i in range(mp.cpu_count())
        ]
        for proc in processes:
            proc.start()
        for proc in processes:
            proc.join()


        #on attend que la queue soit vide
        queue.join()

        listStates = sorted(states.items(), key=lambda l: l[1][1])
        logResultStates(listStates)

        logResultShortcuts(shortcuts)

        print(counter.value)

