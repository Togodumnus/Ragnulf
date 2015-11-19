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

