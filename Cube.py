from utils import Array, codeToColor, codeToGroup, colorize
from numpy import copy as np_copy

PETITS_CUBES = ['FU','FRU','FR','FRD','FD','LFD','FL','LFU','LU','LD',
                'BU','RBU','BR','RBD','BD','BLD','BL','BLU','RU','RD']

COULEURS_SPACE = [' W ', ' B ', ' R ', ' G ', ' O ', ' Y ']

MOUVEMENTS = [
    "U", "Ui", "U'", "U’", "U2",
    "L", "Li", "L'", "L’", "L2",
    "F", "Fi", "F'", "F’", "F2",
    "R", "Ri", "R'", "R’", "R2",
    "B", "Bi", "B'", "B’", "B2",
    "D", "Di", "D'", "D’", "D2",
]

def build_faces(cube, colors=False, space=False):
    """
    build_faces

    Constructions de la représentation des faces du rubik's cube

    :Args:
        cube    {Cube}      Un rubik's cube
        colors  {Boolean}   Utilisation de couleurs pour les terminal ?
                            Defaut False. (mettre à True pour Cube.__str__())
        space   {Boolean}   Espaces entre les facettes ?
                            Defaut False. (mettre à True pour Cube.__str__())

    :Returns:
        {List,List,List,List,List,List,List,List}
                            up, left, front, right, back, down
    """

    up = [
        [cube.cubes['BLU'][2], cube.cubes['BU'][1], cube.cubes['RBU'][2]],
        [cube.cubes['LU'][1],  5,                   cube.cubes['RU'][1]],
        [cube.cubes['LFU'][2], cube.cubes['FU'][1], cube.cubes['FRU'][2]],
    ]

    left = [
        [cube.cubes['BLU'][1], cube.cubes['LU'][0], cube.cubes['LFU'][0]],
        [cube.cubes['BL'][1],  4,                   cube.cubes['FL'][1]],
        [cube.cubes['BLD'][1], cube.cubes['LD'][0], cube.cubes['LFD'][0]],
    ]

    front = [
        [cube.cubes['LFU'][1], cube.cubes['FU'][0], cube.cubes['FRU'][0]],
        [cube.cubes['FL'][0],  1,                   cube.cubes['FR'][0]],
        [cube.cubes['LFD'][1], cube.cubes['FD'][0], cube.cubes['FRD'][0]],
    ]

    right = [
        [cube.cubes['FRU'][1], cube.cubes['RU'][0], cube.cubes['RBU'][0]],
        [cube.cubes['FR'][1],  2,                   cube.cubes['BR'][1]],
        [cube.cubes['FRD'][1], cube.cubes['RD'][0], cube.cubes['RBD'][0]],
    ]

    back = [
        [cube.cubes['RBU'][1], cube.cubes['BU'][0], cube.cubes['BLU'][0]],
        [cube.cubes['BR'][0],  3,                   cube.cubes['BL'][0]],
        [cube.cubes['RBD'][1], cube.cubes['BD'][0], cube.cubes['BLD'][0]],
    ]

    down = [
        [cube.cubes['LFD'][2], cube.cubes['FD'][1], cube.cubes['FRD'][2]],
        [cube.cubes['LD'][1],  0,                   cube.cubes['RD'][1]],
        [cube.cubes['BLD'][2], cube.cubes['BD'][1], cube.cubes['RBD'][2]],
    ]

    #On convertit tous les entiers en la couleur qui leur correspond
    for face in (up, left, front, right, back, down):
        for ligne in range(3):
            for c in range(3):
                #pour chaque case de chaque ligne de chaque face
                if colors:
                    face[ligne][c] = colorize(
                            codeToColor(face[ligne][c]),
                            COULEURS_SPACE if space else None
                        )
                else:
                    face[ligne][c] = codeToColor(face[ligne][c])

    return (up, left, front, right, back, down)

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
        Orange (O) = 4
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

        up, left, front, right, back, down = \
                build_faces(self, colors=True, space=True)

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

    def to_line(self, colors=True):
        """
        to_line

        :Args:
            colors  {Boolean}   Afficher la chaîne en couleur. Defaut True.

        :Returns:
            {String}    la représentation du cube format one line
                        ex: OGRBWYBGBGYYOYOWOWGRYOOOBGBRRYRBWWWRBWYGROWGRYBRGYWBOG
        """

        up, left, front, right, back, down = build_faces(self, colors=colors)

        lines = [[]]*5
        lines[0] = ''.join(sum(up, []))
        lines[4] = ''.join(sum(down, []))

        for i in range(1, 4):
            lines[i] = []
            for face in (left, front, right, back):
                lines[i] += face[i-1]
            lines[i] = ''.join(lines[i])

        return ''.join(lines)

    def edit_cube(self, cube, val):
        '''
        edit_cube

        Édite le cube `cube` avec les données `val` en vérifiant sa validité

        On défini 3 groupes :
            - 0 : Blanc (0) et Jaune (5)
            - 1 : Orange (4) et Rouge (2)
            - 2 : Bleu (1) et Vert (3)

        On ne peut pas retrouver un groupe 0, 1 ou 2 plusieurs fois dans `val`

        :Args:
            cube    {String}    Identifiant du cube dans PETITS_CUBES
            val     {List}      Une liste de 2 ou 3 éléments (selon le cube),
                                entiers, codant la couleur (doivent être déjà validés)

        :Returns:
            {Boolean}           False : les valeurs ne représentent pas un cube
                                correct
        '''
        if not cube in PETITS_CUBES:
            raise ValueError(str(cube) + " n'est pas un petit cube")
        elif not len(cube) == len(val):
            raise ValueError("La taille du cube ne correspond pas")
        else:
            groupes = [0] * 3
            for c in val:
                i = codeToGroup(c)
                if i == None:
                    raise ValueError(str(c) + " n'est pas une couleur")
                else:
                    groupes[i] += 1

            #on garde les groupes qui sont présent plus d'une fois
            #si il y en a, c'est une erreur
            erreurs = [x for x in groupes if x > 1]
            erreur = len(erreurs) > 0

            if not erreur:
                self.cubes[cube] = Array(val)
                return True
            else:
                raise ValueError("Un même groupe de couleur est présent 2 fois")

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

    def rot_L2(self):
        """
        rot_L2

        Rotation double de la face gauche (Left)
        """

        self.cubes['LFD'][0], self.cubes['BLU'][1] = \
        self.cubes['BLU'][1], self.cubes['LFD'][0]

        self.cubes['LFD'][1], self.cubes['BLU'][0] = \
        self.cubes['BLU'][0], self.cubes['LFD'][1]

        self.cubes['LFD'][2], self.cubes['BLU'][2] = \
        self.cubes['BLU'][2], self.cubes['LFD'][2]

        self.cubes['LFU'][0], self.cubes['BLD'][1] = \
        self.cubes['BLD'][1], self.cubes['LFU'][0]

        self.cubes['LFU'][1], self.cubes['BLD'][0] = \
        self.cubes['BLD'][0], self.cubes['LFU'][1]

        self.cubes['LFU'][2], self.cubes['BLD'][2] = \
        self.cubes['BLD'][2], self.cubes['LFU'][2]

        self.cubes['BL'], self.cubes['FL'] = self.cubes['FL'], self.cubes['BL']

        self.cubes['LD'], self.cubes['LU'] = self.cubes['LU'], self.cubes['LD']

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

    def rot_R2(self):
        """
        rot_R2

        Rotation double de la face droite (Right)
        """

        self.cubes['FRD'][0], self.cubes['RBU'][1] = \
        self.cubes['RBU'][1], self.cubes['FRD'][0]

        self.cubes['FRD'][1], self.cubes['RBU'][0] = \
        self.cubes['RBU'][0], self.cubes['FRD'][1]

        self.cubes['FRD'][2], self.cubes['RBU'][2] = \
        self.cubes['RBU'][2], self.cubes['FRD'][2]

        self.cubes['RBD'][0], self.cubes['FRU'][1] = \
        self.cubes['FRU'][1], self.cubes['RBD'][0]

        self.cubes['RBD'][1], self.cubes['FRU'][0] = \
        self.cubes['FRU'][0], self.cubes['RBD'][1]

        self.cubes['RBD'][2], self.cubes['FRU'][2] = \
        self.cubes['FRU'][2], self.cubes['RBD'][2]

        self.cubes['RD'], self.cubes['RU'] = self.cubes['RU'], self.cubes['RD']

        self.cubes['FR'], self.cubes['BR'] = self.cubes['BR'], self.cubes['FR']

    def rot_F(self):
        """
        rot_F

        Rotation de la face avant (Front)
        """

        temp = np_copy(self.cubes['FRU'])

        self.cubes['FRU'][0] = self.cubes['LFU'][1]
        self.cubes['FRU'][1] = self.cubes['LFU'][2]
        self.cubes['FRU'][2] = self.cubes['LFU'][0]

        self.cubes['LFU'][0] = self.cubes['LFD'][2]
        self.cubes['LFU'][1] = self.cubes['LFD'][1]
        self.cubes['LFU'][2] = self.cubes['LFD'][0]

        self.cubes['LFD'][0] = self.cubes['FRD'][2]
        self.cubes['LFD'][1] = self.cubes['FRD'][0]
        self.cubes['LFD'][2] = self.cubes['FRD'][1]

        self.cubes['FRD'][0] = temp[0]
        self.cubes['FRD'][1] = temp[2]
        self.cubes['FRD'][2] = temp[1]

        self.cubes['FU'], self.cubes['FL'], self.cubes['FD'], self.cubes['FR'] \
        = self.cubes['FL'], self.cubes['FD'], self.cubes['FR'], self.cubes['FU']

    def rot_Fi(self):
        """
        rot_Fi

        Rotation inverse de la face avant (Front)
        """

        temp = np_copy(self.cubes['FRD'])

        self.cubes['FRD'][0] = self.cubes['LFD'][1]
        self.cubes['FRD'][1] = self.cubes['LFD'][2]
        self.cubes['FRD'][2] = self.cubes['LFD'][0]

        self.cubes['LFD'][0] = self.cubes['LFU'][2]
        self.cubes['LFD'][1] = self.cubes['LFU'][1]
        self.cubes['LFD'][2] = self.cubes['LFU'][0]

        self.cubes['LFU'][0] = self.cubes['FRU'][2]
        self.cubes['LFU'][1] = self.cubes['FRU'][0]
        self.cubes['LFU'][2] = self.cubes['FRU'][1]

        self.cubes['FRU'][0] = temp[0]
        self.cubes['FRU'][1] = temp[2]
        self.cubes['FRU'][2] = temp[1]

        self.cubes['FL'], self.cubes['FD'], self.cubes['FR'], self.cubes['FU'] \
        = self.cubes['FU'], self.cubes['FL'], self.cubes['FD'], self.cubes['FR']

    def rot_F2(self):
        """
        rot_F2

        Rotation double de la face avant (Front)
        """

        self.cubes['FRD'][0], self.cubes['LFU'][1] = \
        self.cubes['LFU'][1], self.cubes['FRD'][0]

        self.cubes['FRD'][1], self.cubes['LFU'][0] = \
        self.cubes['LFU'][0], self.cubes['FRD'][1]

        self.cubes['FRD'][2], self.cubes['LFU'][2] = \
        self.cubes['LFU'][2], self.cubes['FRD'][2]

        self.cubes['LFD'][0], self.cubes['FRU'][1] = \
        self.cubes['FRU'][1], self.cubes['LFD'][0]

        self.cubes['LFD'][1], self.cubes['FRU'][0] = \
        self.cubes['FRU'][0], self.cubes['LFD'][1]

        self.cubes['LFD'][2], self.cubes['FRU'][2] = \
        self.cubes['FRU'][2], self.cubes['LFD'][2]

        self.cubes['FL'], self.cubes['FR'] = self.cubes['FR'], self.cubes['FL']

        self.cubes['FU'], self.cubes['FD'] = self.cubes['FD'], self.cubes['FU']

    def rot_B(self):
        """
        rot_B

        Rotation de la face arrière (Back)
        """

        temp = np_copy(self.cubes['RBD'])

        self.cubes['RBD'][0] = self.cubes['BLD'][2]
        self.cubes['RBD'][1] = self.cubes['BLD'][0]
        self.cubes['RBD'][2] = self.cubes['BLD'][1]

        self.cubes['BLD'][0] = self.cubes['BLU'][0]
        self.cubes['BLD'][1] = self.cubes['BLU'][2]
        self.cubes['BLD'][2] = self.cubes['BLU'][1]

        self.cubes['BLU'][0] = self.cubes['RBU'][1]
        self.cubes['BLU'][1] = self.cubes['RBU'][2]
        self.cubes['BLU'][2] = self.cubes['RBU'][0]

        self.cubes['RBU'][0] = temp[2]
        self.cubes['RBU'][1] = temp[1]
        self.cubes['RBU'][2] = temp[0]

        self.cubes['BU'], self.cubes['BR'], self.cubes['BD'], self.cubes['BL'] \
        = self.cubes['BR'], self.cubes['BD'], self.cubes['BL'], self.cubes['BU']

    def rot_Bi(self):
        """
        rot_Bi

        Rotation inverse de la face arrière (Back)
        """

        temp = np_copy(self.cubes['RBD'])

        self.cubes['RBD'][0] = self.cubes['RBU'][2]
        self.cubes['RBD'][1] = self.cubes['RBU'][1]
        self.cubes['RBD'][2] = self.cubes['RBU'][0]

        self.cubes['RBU'][0] = self.cubes['BLU'][2]
        self.cubes['RBU'][1] = self.cubes['BLU'][0]
        self.cubes['RBU'][2] = self.cubes['BLU'][1]

        self.cubes['BLU'][0] = self.cubes['BLD'][0]
        self.cubes['BLU'][1] = self.cubes['BLD'][2]
        self.cubes['BLU'][2] = self.cubes['BLD'][1]

        self.cubes['BLD'][0] = temp[1]
        self.cubes['BLD'][1] = temp[2]
        self.cubes['BLD'][2] = temp[0]

        self.cubes['BR'], self.cubes['BD'], self.cubes['BL'], self.cubes['BU'] \
        = self.cubes['BU'], self.cubes['BR'], self.cubes['BD'], self.cubes['BL']

    def rot_B2(self):
        """
        rot_B2

        Rotation double de la face arrière (Back)
        """

        self.cubes['BLD'][0], self.cubes['RBU'][1] = \
        self.cubes['RBU'][1], self.cubes['BLD'][0]

        self.cubes['BLD'][1], self.cubes['RBU'][0] = \
        self.cubes['RBU'][0], self.cubes['BLD'][1]

        self.cubes['BLD'][2], self.cubes['RBU'][2] = \
        self.cubes['RBU'][2], self.cubes['BLD'][2]

        self.cubes['BLU'][0], self.cubes['RBD'][1] = \
        self.cubes['RBD'][1], self.cubes['BLU'][0]

        self.cubes['BLU'][1], self.cubes['RBD'][0] = \
        self.cubes['RBD'][0], self.cubes['BLU'][1]

        self.cubes['BLU'][2], self.cubes['RBD'][2] = \
        self.cubes['RBD'][2], self.cubes['BLU'][2]

        self.cubes['BR'], self.cubes['BL'] = self.cubes['BL'], self.cubes['BR']

        self.cubes['BU'], self.cubes['BD'] = self.cubes['BD'], self.cubes['BU']

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

    def rot_U2(self):
        """
        rot_U2

        Rotation double de la face du haut (Up)
        """

        self.cubes['LFU'], self.cubes['RBU'] = \
        self.cubes['RBU'], self.cubes['LFU']

        self.cubes['FRU'], self.cubes['BLU'] = \
        self.cubes['BLU'], self.cubes['FRU']

        self.cubes['FU'], self.cubes['BU'] = self.cubes['BU'], self.cubes['FU']

        self.cubes['LU'], self.cubes['RU'] = self.cubes['RU'], self.cubes['LU']

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

    def rot_D2(self):
        """
        rot_D2

        Rotation double de la face du bas (Down)
        """

        self.cubes['FRD'], self.cubes['BLD'] = \
        self.cubes['BLD'], self.cubes['FRD']

        self.cubes['RBD'], self.cubes['LFD'] = \
        self.cubes['LFD'], self.cubes['RBD']

        self.cubes['FD'], self.cubes['BD'] = self.cubes['BD'], self.cubes['FD']

        self.cubes['LD'], self.cubes['RD'] = self.cubes['RD'], self.cubes['LD']

    def rot_UF(self):
        """
        rot_UF

        Rotation du cube sur lui même dans le sens Up --> Front
        """
        self.rot_L()
        self.rot_Ri()

        temp = np_copy(self.cubes['FD'])

        self.cubes['FD'][0] = self.cubes['FU'][1]
        self.cubes['FD'][1] = self.cubes['FU'][0]

        self.cubes['FU'][0] = self.cubes['BU'][1]
        self.cubes['FU'][1] = self.cubes['BU'][0]

        self.cubes['BU'][0] = self.cubes['BD'][1]
        self.cubes['BU'][1] = self.cubes['BD'][0]

        self.cubes['BD'][0] = temp[1]
        self.cubes['BD'][1] = temp[0]


    def rot_UR(self):
        """
        rot_UR

        Rotation du cube sur lui même dans le sens Up --> Right
        """
        self.rot_F()
        self.rot_Bi()

        temp = np_copy(self.cubes['RU'])

        self.cubes['RU'][0] = self.cubes['LU'][1]
        self.cubes['RU'][1] = self.cubes['LU'][0]

        self.cubes['LU'][0] = self.cubes['LD'][1]
        self.cubes['LU'][1] = self.cubes['LD'][0]

        self.cubes['LD'][0] = self.cubes['RD'][1]
        self.cubes['LD'][1] = self.cubes['RD'][0]

        self.cubes['RD'][0] = temp[1]
        self.cubes['RD'][1] = temp[0]

    def rot_FR(self):
        """
        rot_FR

        Rotation du cube sur lui même dans le sens Front --> Right
        """
        self.rot_D()
        self.rot_Ui()

        temp = np_copy(self.cubes['FR'])

        self.cubes['FR'][0] = self.cubes['FL'][1]
        self.cubes['FR'][1] = self.cubes['FL'][0]

        self.cubes['FL'][0] = self.cubes['BL'][1]
        self.cubes['FL'][1] = self.cubes['BL'][0]

        self.cubes['BL'][0] = self.cubes['BR'][1]
        self.cubes['BL'][1] = self.cubes['BR'][0]

        self.cubes['BR'][0] = temp[1]
        self.cubes['BR'][1] = temp[0]

    def get_facette(self, petit_cube, indice):
        """
        get_facette

        Récupération de la couleur d'une facette en fonction de son
        son petit cube et de son indice

        :Args:
            petit_cube  {String}    l'identiant du cube. Ex: FRU
            indice      {Int}       0, 1 ou 2 selon le cube (coin ou arête)

        :Returns:
            {Int|String}            La couleur de la facette (codé en Int) ou
                                    un message d'erreur.
        """
        if petit_cube in PETITS_CUBES and indice < len(petit_cube): #On teste les paramètre d'entrée
            return self.cubes[petit_cube][indice]
        else:
            return "Erreur dans les paramètres du getter"

    def cube_contient_couleur(self, petit_cube, c1, c2, c3=None):
        """
        cube_contient_couleur

        Méthode permettant de savoir si les couleurs `c1`, `c2` ou `c3`
        sont présentes dans le cube `petit_cube`.

        :Args:
            petit_cube {String}     Le petit cube qu'il faut regarder
            c1         {int}
            c2         {int}
            c3         {int}        Defaut à None pour le cas d'un cube arrête

        :Returns:
            {Boolean|None}          True si les couleurs sont présentes
                                    None si erreur de `petit_cube`
        """

        if petit_cube in PETITS_CUBES:
            if len(petit_cube) == 2: #On est sur un cube-arrête
                return c1 in self.cubes[petit_cube] \
                        and c2 in self.cubes[petit_cube]
            else:
                return c1 in self.cubes[petit_cube] \
                        and c2 in self.cubes[petit_cube] \
                        and c3 in self.cubes[petit_cube]
        else:
            return None

    def scramble(self, str):
        '''
        scramble

        Effectue la suite de mouvements entrée en paramètre (String) sur le cube

        :Args:
            str {String}    Une suite de mouvements

        :Example:
            c.scramble("R2 D L2 R2 U' L2 D2 R' F' U L2 D F R' U L2 R U' R2")

        :Returns:
            {Boolean|None}      True si pas d'erreurs dans la chaîne et toutes
                                les rotations ont bien étées effectuées.
                                None si erreur.
        '''
        mvt = str.split() #on découpe la chaîne en mots
        return self.mouvements(mvt)

    def mouvements(self, mvt):
        '''
        mouvements

        Effectue la suite de mouvements entrée en paramètre (Itérable) sur le cube

        :Args:
            mvt {List|Tuple}    Une suite de mouvements

        :Example:
            c.mouvements(('F2', Ri'))

        :Returns:
            {Boolean|None}      True si pas d'erreurs dans la chaîne et toutes
                                les rotations ont bien étées effectuées.
                                None si erreur.
        '''

        for c in mvt: #pour chaque mouvement
            if c in MOUVEMENTS:
                if len(c) == 2:
                    if c[1] == "'" or c[1] == "’": #on traduit le ' en i (R' va devenir rot_Ri)
                        c = c[0] + 'i'


                #on exécute la méthode qui va bien
                methodToCall = getattr(self, 'rot_' + c)
                methodToCall()

            else:
                return None

        return True

    def face_resolu(self,face):
        """
        face_resolu

        Fonction qui dit si une face du cube (passé en paramètre) est résolu ou non

        :Args:
            face {Sting}    une face du cube

        :Example:
            c.face_resolu(('U')

        :Returns:
            {Boolean}      True toute la face correspond à sa couleur
                           False sinon
        """
        if face == 'U': # Si la face Up du cube
            # On récupère toutes ma facettes de la face
            faceJaune = (
                self.get_facette('FU',1),
                self.get_facette('RU',1),
                self.get_facette('BU',1),
                self.get_facette('LU',1),
                self.get_facette('LFU',2),
                self.get_facette('FRU',2),
                self.get_facette('RBU',2),
                self.get_facette('BLU',2),

            )
            return faceJaune == (5,5,5,5,5,5,5,5) # Test si toute les facettes sont jaune
        elif face == 'D': # Si la face Down du cube
            # On récupère toutes ma facettes de la face
            faceBlanche = (
                self.get_facette('FD',1),
                self.get_facette('RD',1),
                self.get_facette('BD',1),
                self.get_facette('LD',1),
                self.get_facette('LFD',2),
                self.get_facette('FRD',2),
                self.get_facette('RBD',2),
                self.get_facette('BLD',2),
            )
            return faceBlanche == (0,0,0,0,0,0,0,0)
        elif face == 'B': # Si la face Back du cube
            # On récupère toutes ma facettes de la face
            faceVerte  = (
                self.get_facette('BU',0),
                self.get_facette('BL',0),
                self.get_facette('BR',0),
                self.get_facette('BD',0),
                self.get_facette('BLU',0),
                self.get_facette('BLU',0),
                self.get_facette('RBU',1),
                self.get_facette('RBD',1),
            )
            return faceVerte == (3,3,3,3,3,3,3,3) # Test si toute les facettes sont verte
        elif face == 'F': # Si la face Front du cube
            # On récupère toutes ma facettes de la face
            faceBleue = (
                self.get_facette('FU',0),
                self.get_facette('FR',0),
                self.get_facette('FL',0),
                self.get_facette('FD',0),
                self.get_facette('FRU',0),
                self.get_facette('FRD',0),
                self.get_facette('LFD',1),
                self.get_facette('LFU',1),
            )
            return faceBleue == (1,1,1,1,1,1,1,1) # Test si toute les facettes sont bleue
        elif face == "R": # Si la face Right du cube
            # On récupère toutes ma facettes de la face
            faceRouge = (
                self.get_facette('RU',0),
                self.get_facette('RD',0),
                self.get_facette('FR',1),
                self.get_facette('BR',1),
                self.get_facette('FRU',1),
                self.get_facette('FRD',1),
                self.get_facette('RBU',0),
                self.get_facette('RBD',0),
            )
            return faceRouge == (2,2,2,2,2,2,2,2) # Test si toute les facettes sont rouge
        elif face == "L": # Si la face Left du cube
            # On récupère toutes ma facettes de la face
            faceOrange = (
                self.get_facette('LU',0),
                self.get_facette('LD',0),
                self.get_facette('LFD',0),
                self.get_facette('LFU',0),
                self.get_facette('FL',1),
                self.get_facette('BLD',1),
                self.get_facette('BLU',1),
                self.get_facette('BL',1),
            )
            return faceOrange == (4,4,4,4,4,4,4,4) # Test si toute les facettes sont orange
        else:
            return "Erreur dans les paramètres de la fonction"



if __name__ == '__main__':

    # Exemple d'utilisation du Cube
    c = Cube() #par défaut, ce cube est résolu
    print(c)
    #Test fonction face_resolu
    print(c.face_resolu("U"))
    print(c.face_resolu("D"))
    print(c.face_resolu("B"))
    print(c.face_resolu("F"))
    print(c.face_resolu("L"))
    print(c.face_resolu("R"))

    print(c.to_line())
    print('Couleur facette BLD/indice 0 : ' + str(c.get_facette('BLD',0))) #test du getter


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

    print('rot_L2')
    c = Cube()
    c.rot_L2()
    print(c)

    print('rot_R')
    c = Cube()
    c.rot_R()
    print(c)

    print('rot_Ri')
    c = Cube()
    c.rot_Ri()
    print(c)

    print('rot_R2')
    c = Cube()
    c.rot_R2()
    print(c)

    print('rot_F')
    c = Cube()
    c.rot_F()
    print(c)

    print('rot_Fi')
    c = Cube()
    c.rot_Fi()
    print(c)

    print('rot_F2')
    c = Cube()
    c.rot_F2()
    print(c)

    print('rot_B')
    c = Cube()
    c.rot_B()
    print(c)

    print('rot_Bi')
    c = Cube()
    c.rot_Bi()
    print(c)

    print('rot_B2')
    c = Cube()
    c.rot_B2()
    print(c)

    print('rot_U')
    c = Cube()
    c.rot_U()
    print(c)

    print('rot_Ui')
    c = Cube()
    c.rot_Ui()
    print(c)

    print('rot_U2')
    c = Cube()
    c.rot_U2()
    print(c)


    print('rot_D')
    c = Cube()
    c.rot_D()
    print(c)

    print('rot_Di')
    c = Cube()
    c.rot_Di()
    print(c)

    print('rot_D2')
    c = Cube()
    c.rot_D2()
    print(c)


    print('rot_UF')
    c = Cube()
    c.rot_UF()
    print(c)

    print('rot_UR')
    c = Cube()
    c.rot_UR()
    print(c)

    print('rot_FR')
    c = Cube()
    c.rot_FR()
    print(c)
