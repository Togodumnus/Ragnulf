import numpy as np

COULEURS = ['W', 'B', 'R', 'G', 'O', 'Y']

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

def codeToColor(code):
    """
    codeToColor

    Convertit un code entier en la couleur qui respond

    :Args:
        code    {Int}   {0, 1, ... 5}

    :Return:
        {String|None}        La couleur en anglais dans
                             {'W', 'B', 'R', 'G', 'O', 'Y'}.
                             None si erreur de code.
    """
    if code < 6 and code > -1:
        return COULEURS[code]
    else:
        return None

def colorToCode(color):
    """
    codeToColor

    Convertit la str couleur (W,O..) au code correspondant

    :Args:
        code    {Str}   {'W', 'B', 'R', 'G', 'O', 'Y'}

    :Return:
        {Int|None}        Le code associé à la couleur
    """
    return COULEURS.index(color) if color in COULEURS else None

def codeToGroup(code):
    '''
    codeToGroup

    On défini 3 groupes :
        - 0 : Blanc (0) et Jaune (5)
        - 1 : Orange (4) et Rouge (2)
        - 2 : Bleu (1) et Vert (3)

    Ils servent à valider un petit cube

    :Args:
        code    {Int}   La couleur dans {0, 1 ... 5}

    :Return:
        {Int}       Le groupe
    '''
    if code == 0 or code == 5:
        return 0
    elif code == 4 or code == 2:
        return 1
    elif code == 1 or code == 3:
        return 2
    else:
        return None


