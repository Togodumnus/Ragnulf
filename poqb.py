from Cube import Cube
from utils import Array, colorize, translate_mvt
from algo import algo_cfop
from lire_entree import lecture_cube


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
    c = lecture_cube(cube_c54)[1]
    manoeuvre = algo_cfop(c)
    
    return manoeuvre


if __name__=="__main__":
    cube = 'OGRBWYBGBGYYOYOWOWGRYOOOBGBRRYRBWWWRBWYGROWGRYBRGYWBOG'
    print('Résolution de :', "".join([colorize(x) for x in cube]))
    resolution = solve(cube)
    resolution = " ".join([translate_mvt(x) for x in resolution])
    print ("Exécuter la manoeuvre {}".format(resolution))


