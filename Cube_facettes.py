from utils import Array, codeToColor
from numpy import copy as np_copy

class Cube():
    """
    Cube

    La structure de donnée modélisant un cube ainsi que les fonctions de
    rotations qui s'y appliquent

    @see https://gitlab.univ-nantes.fr/E132397K/Ragnulf/issues/4 pour
    l'histoirique des choix effectués

    Codage des couleurs :
        White  (W) = 0
        Blue   (B) = 1
        Red    (R) = 2
        Green  (G) = 3
        Orange (0) = 4
        Yellow (Y) = 5

    Convention des couleurs des faces :
        Down  - White
        Front - Blue
        Right - Red
        Back  - Green
        Left  - Orange
        Up    - Yellow
    """

	def __init__(self):
        """
        __init__

        Création d'une nouvelle instance de Cube
        """

        self.cubes = Array([5,5,5,5,5,5,5,5,
        	4,4,4,4,4,4,4,4,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3
        					0,0,0,0,0,0,0,0])
        