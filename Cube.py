from utils import Array, codeToColor

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

    def __str__(self):
        """
        On veut retourner une chaîne du genre:
                   O G R
                   B W Y
                   B G B
            G Y Y  O Y O  W O W  G R Y
            O O O  B G B  R R Y  R B W
            W W R  B W Y  G R O  W G R
                   Y B R
                   G Y W
                   B O G
        """

        #Un carré d'espaces pour les blocs vides du patron ci-dessus
        empty = [
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' ']
        ]

        up = [
            [self.cubes['BLU'][2], self.cubes['BU'][1], self.cubes['BRU'][2]],
            [self.cubes['LU'][1],  5,                   self.cubes['LR'][1]],
            [self.cubes['FLU'][2], self.cubes['FU'][1], self.cubes['FRU'][2]],
        ]

        left = [
            [self.cubes['BLU'][1], self.cubes['LU'][0], self.cubes['FLU'][1]],
            [self.cubes['BL'][1],  4,                   self.cubes['FL'][1]],
            [self.cubes['BLD'][1], self.cubes['LD'][0], self.cubes['FLD'][1]],
        ]

        front = [
            [self.cubes['FLU'][0], self.cubes['FU'][0], self.cubes['FRU'][0]],
            [self.cubes['FL'][0],  1,                   self.cubes['FR'][0]],
            [self.cubes['FLD'][0], self.cubes['FD'][0], self.cubes['FRD'][0]],
        ]

        right = [
            [self.cubes['FRU'][1], self.cubes['RU'][0], self.cubes['BRU'][1]],
            [self.cubes['FR'][1],  2,                   self.cubes['BR'][1]],
            [self.cubes['FRD'][1], self.cubes['RD'][0], self.cubes['BRD'][1]],
        ]

        back = [
            [self.cubes['BRU'][0], self.cubes['BU'][0], self.cubes['BLU'][0]],
            [self.cubes['BR'][0],  3,                   self.cubes['BL'][0]],
            [self.cubes['BRD'][0], self.cubes['BD'][0], self.cubes['BLD'][0]],
        ]

        down = [
            [self.cubes['FLD'][2], self.cubes['FD'][1], self.cubes['FRD'][2]],
            [self.cubes['LD'][1],  0,                   self.cubes['RD'][1]],
            [self.cubes['BLD'][2], self.cubes['BD'][1], self.cubes['BRD'][2]],
        ]



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
