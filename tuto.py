from time import sleep
from utils import clear, readArgs, colorize, translate_mvt, newGetch, TermColors
from algo import algo_cfop
from images_ascii import aideMouvements

SPEED = 2 #écrans / sec

def tuto(cube, mouvements):
    """
    tuto

    :Args:
        cube        {Cube}      Un cube à la sortie de lecture_cube
        mouvements  {List}      Suite de mouvements à appliquer sur le cube
                                pour le résoudre, calculée par algo_cfop()
    """

    #lecture des paramètres
    params = readArgs()
    speed = float(params['speed']) if 'speed' in params else SPEED

    resolution = " ".join([translate_mvt(x) for x in mouvements])

    mouvementsDone = []
    mouvementsRestants = list(mouvements)

    clear()
    if 'auto' in params:
        print('Positionnez la face bleue face à vous et la face blanche face au sol, face jaune au dessus\n')
        print('le tuto en mode auto va bientôt commencer, tenez vous prêt !!!')
        sleep(3)
    clear()
    sleep(1)
    print("Exécution de la manoeuvre : {}".format(resolution) )
    print(cube)

    for m in mouvements:
        clear()
        mouvementsRestants.remove(m)
        method = getattr(cube, 'rot_' + m)
        method()

        print(
            "Exécution de la manoeuvre : "

            #les mouvements effectués
            + TermColors.green + \
            "{}".format(" ".join([translate_mvt(x) for x in mouvementsDone]))+ \
            TermColors.end + ' ' +

            #le mouvement actuel
            TermColors.bgGreen + translate_mvt(m) + TermColors.end + \

            #les mouvements restant
            " {}".format(" ".join([translate_mvt(x) \
                for x in mouvementsRestants])
            ) + '\n'
        )

        if 'moves' not in params:
            print(cube)
        else:
            #L'utilisateur a demandé de voir l'aide des mouvements
            print(aideMouvements(cube, m))
            print("Rotation : ", translate_mvt(m) +'\n\n')

        mouvementsDone.append(m)

        if 'auto' not in params:
            print('Press any key to continue . . .\n')
            newGetch()
        else:
            sleep(1 / speed)

if __name__ == '__main__':
    from lire_entree import lecture_cube
    cube = 'OGRBWYBGBGYYOYOWOWGRYOOOBGBRRYRBWWWRBWYGROWGRYBRGYWBOG'
    error, c = lecture_cube(cube)
    if error:
        raise Error(error)

    c0 = c.copy()

    mouvements = algo_cfop(c)

    tuto(c0, mouvements)
