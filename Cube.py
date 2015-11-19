import numpy as np

def Array(arr):
    """
    Array

    Un raccourcis pour np.array(arr, dtype=np.int8)

    :Args:
        arr {List}  Une liste pour initialiser le tableau

    :Returns:
        {np.array}  Un tableau numpy prévu pour contenir des entier 8 bits
    """
    return np.array(arr, dtype=np.int8)

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

        self.cubes = {
            #Front
            'FU'  : Array([]),
            'FRU' : Array([]),
            'FR'  : Array([]),
            'FRD' : Array([]),
            'FD'  : Array([]),
            'FLD' : Array([]),
            'FL'  : Array([]),
            'FLU' : Array([]),

            #Left
            'LU'  : Array([]),
            'LD'  : Array([]),

            #Back
            'BU'  : Array([]),
            'BRU' : Array([]),
            'BR'  : Array([]),
            'BRD' : Array([]),
            'BD'  : Array([]),
            'BLD' : Array([]),
            'BL'  : Array([]),
            'BLU' : Array([]),

            #Right
            'RU'  : Array([]),
            'RD'  : Array([]),

        }


    def rot_L():
        """
        rot_L

        Rotation de la face gauche (Left)
        """
        #TODO
        pass

    def rot_Li():
        """
        rot_Li

        Rotation inverse de la face gauche (Left)
        """
        #TODO
        pass

    def rot_R():
        """
        rot_R

        Rotation de la face droite (Right)
        """
        #TODO
        pass

    def rot_Ri():
        """
        rot_Ri

        Rotation inverse de la face droite (Right)
        """
        #TODO
        pass

    def rot_F():
        """
        rot_F

        Rotation de la face avant (Front)
        """
        #TODO
        pass

    def rot_Fi():
        """
        rot_Fi

        Rotation inverse de la face avant (Front)
        """
        #TODO
        pass

    def rot_B():
        """
        rot_B

        Rotation de la face arrière (Back)
        """
        #TODO
        pass

    def rot_Bi():
        """
        rot_Bi

        Rotation inverse de la face arrière (Back)
        """
        #TODO
        pass

    def rot_U():
        """
        rot_U

        Rotation de la face du haut (Up)
        """
        #TODO
        pass

    def rot_Li():
        """
        rot_Ui

        Rotation inverse de la face du haut (Up)
        """
        #TODO
        pass

    def rot_D():
        """
        rot_D

        Rotation de la face du bas (Down)
        """
        #TODO
        pass

    def rot_Di():
        """
        rot_Di

        Rotation inverse de la face du bas (Down)
        """
        #TODO
        pass
