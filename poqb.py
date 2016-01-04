from Cube import Cube
from utils import Array, colorize, translate_mvt, readArgs
from algo import algo_cfop
from lire_entree import lecture_cube

DEFAULT_CUBE = 'OGRBWYBGBGYYOYOWOWGRYOOOBGBRRYRBWWWRBWYGROWGRYBRGYWBOG'

def solve(cube_c54):
    """La fonction principale du projet qui résoud un Rubik's Cube.

    :param cube_c54: passé sous sa forme '54 facettes colorées'
           O G R
           B W Y
           B G B
    G Y Y  O Y O  W O W  G R Y
    O O O  B G B  R R Y  R B W
    W W R  B W Y  G R O  W G R
           Y B R
           G Y W
           B O G
    :return: une chaîne de caractères qui encode la manoeuvre
    qui mène du cube de départ à la permutation monochrome.

    :Example:

    solve('OGRBWYBGBGYYOYOWOWGRYOOOBGBRRYRBWWWRBWYGROWGRYBRGYWBOG')

    """
    manoeuvre = ""
    err = False
    if lecture_cube(cube_c54)[0]:
        err = True
    else:
        c = lecture_cube(cube_c54)[1]
        manoeuvre = algo_cfop(c)

    return err, manoeuvre

if __name__=="__main__":
    """
    :Example:
        python poqb.py
        python poqb.py -c YYYYYYYYYOOOBBBRRRGGGOOOBBBRRRGGGOOOBBBRRRGGGWWWWWWWWW
        python poqb.py --cube=YYYYYYYYYOOOBBBRRRGGGOOOBBBRRRGGGOOOBBBRRRGGGWWWWWWWWW
    """

    #On récupère le cube en paramètre ou on utilise celui par défaut
    params = readArgs()
    cube = str(params['cube']) if 'cube' in params else DEFAULT_CUBE

    err, resolution = solve(cube)
    if err:
        print("Erreur dans la lecture du cube : cube non valide")
    else:
        print('Résolution de :', "".join([colorize(x) for x in cube]))
        resolution = solve(cube)[1]
        resolution = " ".join([translate_mvt(x) for x in resolution])
        print("Exécuter la manoeuvre {}".format(resolution))
