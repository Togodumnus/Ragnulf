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
        return couleurs[code]
    else:
        return None
