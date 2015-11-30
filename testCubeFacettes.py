from random import shuffle
from Cube_facettes import Cube

rotations = ['U', 'Ui', 'D', 'Di', 'B', 'Bi', 'F', 'Fi', 'L', 'Li', 'R', 'Ri']

def test():
    """
    test

    Test du temps d'exécution des rotations pour la modélisation du Cube
    par ces petits cubes

    :Example:
        $ time python testCubeFacettes.py
        $ python -m cProfile -s time testCube.py | lFacettesess
    """

    c = Cube()
    shuffle(rotations) #on mélange la liste
    for r in rotations * 12: #on la duplique 12 fois
        rotation = getattr(c, 'rot_' + r) #on va chercher la fonction de rotation
        rotation()

if __name__ == '__main__':
    test()

