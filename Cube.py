from utils import Array, codeToColor, colorize
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

        self.cubes = {

            #1ère couronne
            'FU' : Array([1, 5]),
            'FRU': Array([1, 2, 5]),
            'RU' : Array([2, 5]),
            'RBU': Array([2, 3, 5]),
            'BU' : Array([3, 5]),
            'BLU': Array([3, 4, 5]),
            'LU' : Array([4, 5]),
            'LFU': Array([4, 1, 5]),

            #2ème couronne
            'FR' : Array([1, 2]),
            'BR' : Array([3, 2]),
            'BL' : Array([3, 4]),
            'FL' : Array([1, 4]),

            #3ème couronne
            'FD' : Array([1, 0]),
            'FRD': Array([1, 2, 0]),
            'RD' : Array([2, 0]),
            'RBD': Array([2, 3, 0]),
            'BD' : Array([3, 0]),
            'BLD': Array([3, 4, 0]),
            'LD' : Array([4, 0]),
            'LFD': Array([4, 1, 0]),
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

        #Un espace pour constuire le patro ci-dessus
        space = [' ']

        #Une lignes d'espaces pour les blocs vides du patron ci-dessus
        empty = space * 9

        up = [
            [self.cubes['BLU'][2], self.cubes['BU'][1], self.cubes['RBU'][2]],
            [self.cubes['LU'][1],  5,                   self.cubes['RU'][1]],
            [self.cubes['LFU'][2], self.cubes['FU'][1], self.cubes['FRU'][2]],
        ]

        left = [
            [self.cubes['BLU'][1], self.cubes['LU'][0], self.cubes['LFU'][0]],
            [self.cubes['BL'][1],  4,                   self.cubes['FL'][1]],
            [self.cubes['BLD'][1], self.cubes['LD'][0], self.cubes['LFD'][0]],
        ]

        front = [
            [self.cubes['LFU'][1], self.cubes['FU'][0], self.cubes['FRU'][0]],
            [self.cubes['FL'][0],  1,                   self.cubes['FR'][0]],
            [self.cubes['LFD'][1], self.cubes['FD'][0], self.cubes['FRD'][0]],
        ]

        right = [
            [self.cubes['FRU'][1], self.cubes['RU'][0], self.cubes['RBU'][0]],
            [self.cubes['FR'][1],  2,                   self.cubes['BR'][1]],
            [self.cubes['FRD'][1], self.cubes['RD'][0], self.cubes['RBD'][0]],
        ]

        back = [
            [self.cubes['RBU'][1], self.cubes['BU'][0], self.cubes['BLU'][0]],
            [self.cubes['BR'][0],  3,                   self.cubes['BL'][0]],
            [self.cubes['RBD'][1], self.cubes['BD'][0], self.cubes['BLD'][0]],
        ]

        down = [
            [self.cubes['LFD'][2], self.cubes['FD'][1], self.cubes['FRD'][2]],
            [self.cubes['LD'][1],  0,                   self.cubes['RD'][1]],
            [self.cubes['BLD'][2], self.cubes['BD'][1], self.cubes['RBD'][2]],
        ]

        #On convertit tous les entiers en la couleur qui leur correspond
        for face in [up, left, front, right, back, down]:
            for ligne in range(3):
                for c in range(3):
                    #pour chaque case de chaque ligne de chaque face
                    face[ligne][c] = colorize(codeToColor(face[ligne][c]))

        result = [] #tableau de toutes les lignes à afficher

        #les 3 premières lignes, il n'y a que la face up
        for i in range(3):
            result.append(empty + space + up[i] + space + empty + space + empty)

        #les 3 lignes suivantes, il y a left, front, right et back
        for i in range(3):
            result.append(left[i] + space + front[i] + space + right[i] + \
                    space + back[i])

        #les 3 dernières lignes, il y a que la face down
        for i in range(3):
            result.append(empty + space + down[i] + space + empty)

        return '\n'.join(''.join(l) for l in result) #on convertit la liste en chaîne


    def rot_L(self):
        """
        rot_L

        Rotation de la face gauche (Left)
        """

        temp = np_copy(self.cubes['LFD'])

        self.cubes['LFD'][0] = self.cubes['LFU'][0]
        self.cubes['LFD'][1] = self.cubes['LFU'][2]
        self.cubes['LFD'][2] = self.cubes['LFU'][1]

        self.cubes['LFU'][0] = self.cubes['BLU'][1]
        self.cubes['LFU'][1] = self.cubes['BLU'][2]
        self.cubes['LFU'][2] = self.cubes['BLU'][0]

        self.cubes['BLU'][0] = self.cubes['BLD'][2]
        self.cubes['BLU'][1] = self.cubes['BLD'][1]
        self.cubes['BLU'][2] = self.cubes['BLD'][0]

        self.cubes['BLD'][0] = temp[2]
        self.cubes['BLD'][1] = temp[0]
        self.cubes['BLD'][2] = temp[1]

        temp = np_copy(self.cubes['LD'])

        self.cubes['LD'][0] = self.cubes['FL'][1]
        self.cubes['LD'][1] = self.cubes['FL'][0]

        self.cubes['FL'][0] = self.cubes['LU'][1]
        self.cubes['FL'][1] = self.cubes['LU'][0]

        self.cubes['LU'][0] = self.cubes['BL'][1]
        self.cubes['LU'][1] = self.cubes['BL'][0]

        self.cubes['BL'][0] = temp[1]
        self.cubes['BL'][1] = temp[0]

    def rot_Li(self):
        """
        rot_Li

        Rotation inverse de la face gauche (Left)
        """

        temp = np_copy(self.cubes['BLU'])

        self.cubes['BLU'][0] = self.cubes['LFU'][2]
        self.cubes['BLU'][1] = self.cubes['LFU'][0]
        self.cubes['BLU'][2] = self.cubes['LFU'][1]

        self.cubes['LFU'][0] = self.cubes['LFD'][0]
        self.cubes['LFU'][1] = self.cubes['LFD'][2]
        self.cubes['LFU'][2] = self.cubes['LFD'][1]

        self.cubes['LFD'][0] = self.cubes['BLD'][1]
        self.cubes['LFD'][1] = self.cubes['BLD'][2]
        self.cubes['LFD'][2] = self.cubes['BLD'][0]

        self.cubes['BLD'][0] = temp[2]
        self.cubes['BLD'][1] = temp[1]
        self.cubes['BLD'][2] = temp[0]

        temp = np_copy(self.cubes['LD'])

        self.cubes['LD'][0] = self.cubes['BL'][1]
        self.cubes['LD'][1] = self.cubes['BL'][0]

        self.cubes['BL'][0] = self.cubes['LU'][1]
        self.cubes['BL'][1] = self.cubes['LU'][0]

        self.cubes['LU'][0] = self.cubes['FL'][1]
        self.cubes['LU'][1] = self.cubes['FL'][0]

        self.cubes['FL'][0] = temp[1]
        self.cubes['FL'][1] = temp[0]

    def rot_R(self):
        """
        rot_R

        Rotation de la face droite (Right)
        """

        temp = np_copy(self.cubes['RBU'])

        self.cubes['RBU'][0] = self.cubes['FRU'][1]
        self.cubes['RBU'][1] = self.cubes['FRU'][2]
        self.cubes['RBU'][2] = self.cubes['FRU'][0]

        self.cubes['FRU'][0] = self.cubes['FRD'][2]
        self.cubes['FRU'][1] = self.cubes['FRD'][1]
        self.cubes['FRU'][2] = self.cubes['FRD'][0]

        self.cubes['FRD'][0] = self.cubes['RBD'][2]
        self.cubes['FRD'][1] = self.cubes['RBD'][0]
        self.cubes['FRD'][2] = self.cubes['RBD'][1]

        self.cubes['RBD'][0] = temp[0]
        self.cubes['RBD'][1] = temp[2]
        self.cubes['RBD'][2] = temp[1]

        temp = np_copy(self.cubes['RD'])

        self.cubes['RD'][0] = self.cubes['BR'][1]
        self.cubes['RD'][1] = self.cubes['BR'][0]

        self.cubes['BR'][0] = self.cubes['RU'][1]
        self.cubes['BR'][1] = self.cubes['RU'][0]

        self.cubes['RU'][0] = self.cubes['FR'][1]
        self.cubes['RU'][1] = self.cubes['FR'][0]

        self.cubes['FR'][0] = temp[1]
        self.cubes['FR'][1] = temp[0]

    def rot_Ri(self):
        """
        rot_Ri

        Rotation inverse de la face droite (Right)
        """

        temp = np_copy(self.cubes['FRD'])

        self.cubes['FRD'][0] = self.cubes['FRU'][2]
        self.cubes['FRD'][1] = self.cubes['FRU'][1]
        self.cubes['FRD'][2] = self.cubes['FRU'][0]

        self.cubes['FRU'][0] = self.cubes['RBU'][2]
        self.cubes['FRU'][1] = self.cubes['RBU'][0]
        self.cubes['FRU'][2] = self.cubes['RBU'][1]

        self.cubes['RBU'][0] = self.cubes['RBD'][0]
        self.cubes['RBU'][1] = self.cubes['RBD'][2]
        self.cubes['RBU'][2] = self.cubes['RBD'][1]

        self.cubes['RBD'][0] = temp[1]
        self.cubes['RBD'][1] = temp[2]
        self.cubes['RBD'][2] = temp[0]

        temp = np_copy(self.cubes['RD'])

        self.cubes['RD'][0] = self.cubes['FR'][1]
        self.cubes['RD'][1] = self.cubes['FR'][0]

        self.cubes['FR'][0] = self.cubes['RU'][1]
        self.cubes['FR'][1] = self.cubes['RU'][0]

        self.cubes['RU'][0] = self.cubes['BR'][1]
        self.cubes['RU'][1] = self.cubes['BR'][0]

        self.cubes['BR'][0] = temp[1]
        self.cubes['BR'][1] = temp[0]

    def rot_F(self):
        """
        rot_F

        Rotation de la face avant (Front)
        """
        self.cubes['FRU'], self.cubes['FRD'], self.cubes['FLD'], self.cubes['FLU'] = self.cubes['FRD'],self.cubes['FLD'], self.cubes['FLU'], self.cubes['FRU']
        self.cubes['FU'], self.cubes['FR'], self.cubes['FD'], self.cubes['FL'] = self.cubes['FR'],self.cubes['FD'], self.cubes['FL'], self.cubes['FU']

    def rot_Fi(self):
        """
        rot_Fi

        Rotation inverse de la face avant (Front)
        """
        self.cubes['FRD'],self.cubes['FLD'], self.cubes['FLU'], self.cubes['FRU'] = self.cubes['FRU'], self.cubes['FRD'], self.cubes['FLD'], self.cubes['FLU']
        self.cubes['FR'],self.cubes['FD'], self.cubes['FL'], self.cubes['FU'] = self.cubes['FU'], self.cubes['FR'], self.cubes['FD'], self.cubes['FL']

    def rot_B(self):

        """
        rot_B

        Rotation de la face arrière (Back)
        """
        self.cubes['BRU'],self.cubes['BRD'], self.cubes['BLD'], self.cubes['BLU'] = self.cubes['BRD'], self.cubes['BLD'], self.cubes['BLU'], self.cubes['BRU']
        self.cubes['BR'],self.cubes['BD'], self.cubes['BL'], self.cubes['BU'] = self.cubes['BD'], self.cubes['BL'], self.cubes['BU'], self.cubes['BR']

    def rot_Bi(self):
        """
        rot_Bi

        Rotation inverse de la face arrière (Back)
        """
        #TODO
        pass

    def rot_U(self):
        """
        rot_U

        Rotation de la face du haut (Up)
        """
        self.cubes['FRU'], self.cubes['RBU'], self.cubes['BLU'], self.cubes['LFU'] \
            = self.cubes['RBU'], self.cubes['BLU'], self.cubes['LFU'], self.cubes['FRU']

        self.cubes['FU'], self.cubes['RU'], self.cubes['BU'], self.cubes['LU'] \
            = self.cubes['RU'],self.cubes['BU'], self.cubes['LU'], self.cubes['FU']

    def rot_Ui(self):
        """
        rot_Ui

        Rotation inverse de la face du haut (Up)
        """
        self.cubes['FRU'], self.cubes['RBU'], self.cubes['BLU'], self.cubes['LFU'] \
            = self.cubes['LFU'], self.cubes['FRU'], self.cubes['RBU'], self.cubes['BLU']

        self.cubes['FU'], self.cubes['RU'], self.cubes['BU'], self.cubes['LU'] \
            = self.cubes['LU'],self.cubes['FU'], self.cubes['RU'], self.cubes['BU']

    def rot_D(self):
        """
        rot_D

        Rotation de la face du bas (Down)
        """
        self.cubes['FRD'], self.cubes['RBD'], self.cubes['BLD'], self.cubes['LFD'] \
            = self.cubes['LFD'], self.cubes['FRD'], self.cubes['RBD'], self.cubes['BLD']

        self.cubes['FD'], self.cubes['RD'], self.cubes['BD'], self.cubes['LD'] \
            = self.cubes['LD'],self.cubes['FD'], self.cubes['RD'], self.cubes['BD']

    def rot_Di(self):
        """
        rot_Di

        Rotation inverse de la face du bas (Down)
        """
        self.cubes['FRD'], self.cubes['RBD'], self.cubes['BLD'], self.cubes['LFD'] \
            = self.cubes['RBD'], self.cubes['BLD'], self.cubes['LFD'], self.cubes['FRD']

        self.cubes['FD'], self.cubes['RD'], self.cubes['BD'], self.cubes['LD'] \
            = self.cubes['RD'],self.cubes['BD'], self.cubes['LD'], self.cubes['FD']

if __name__ == '__main__':

    # Exemple d'utilisation du Cube
    c = Cube() #par défaut, ce cube est résolu
    print(c)

    print(c.cubes['FRU'], type(c.cubes['FRU'])) #<calss 'numpy.ndarray'>
    c.cubes['FRU'] = Array([0, 1, 2]) #on remplit avec les couleurs qui vont bien
    c.cubes['FRU'][0] = 4             #ou
    print(c.cubes['FRU'])

    print('Test rotations')

    print('rot_L')
    c = Cube()
    c.rot_L()
    print(c)

    print('rot_Li')
    c = Cube()
    c.rot_Li()
    print(c)

    print('rot_R')
    c = Cube()
    c.rot_R()
    print(c)

    print('rot_Ri')
    c = Cube()
    c.rot_Ri()
    print(c)

    print('rot_U')
    c = Cube()
    c.rot_U()
    print(c)

    print('rot_Ui')
    c = Cube()
    c.rot_Ui()
    print(c)

    print('rot_D')
    c = Cube()
    c.rot_D()
    print(c)

    print('rot_Di')
    c = Cube()
    c.rot_Di()
    print(c)
