import numpy as np
from os import name as os_name

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


class unixTermColors():
    """
    unixTermColors

    :Source:
        http://kishorelive.com/2011/12/05/printing-colors-in-the-terminal/
    """
    black  = '\033[38;5;232m'
    blue   = '\033[38;5;18m'
    red    = '\033[38;5;124m'
    green  = '\033[38;5;22m'
    orange = '\033[38;5;202m'
    yellow = '\033[38;5;220m'
    white  = '\033[38;5;255m'

    bgBlack  = '\033[48;5;232m'
    bgBlue   = '\033[48;5;18m'
    bgRed    = '\033[48;5;124m'
    bgGreen  = '\033[48;5;22m'
    bgOrange = '\033[48;5;202m'
    bgYellow = '\033[48;5;220m'
    bgWhite  = '\033[48;5;255m'

    bold      = '\033[1m'
    underline = '\033[4m'
    blink     = '\033[5m'
    inverse   = '\033[7m'
    hidden    = '\033[8m'

    end      = '\033[m'

    def __init__(self):
        pass

class winTermColors():
    """
    winTermColors
    """
    #TODO

    bgBlack  = ''
    bgBlue   = ''
    bgRed    = ''
    bgGreen  = ''
    bgOrange = ''
    bgYellow = ''
    bgWhite  = ''
    end      = ''

    def __init__(self):
        pass

#Windows n'aime pas trop les couleurs ascii
TermColors = winTermColors() if os_name == 'nt' else unixTermColors()

if __name__ == '__main__':
    print("Test unixTermColors")
    c = unixTermColors()

    print('black', c.black + "hello" + c.end)
    print('blue', c.blue + "hello" + c.end)
    print('red', c.red + "hello" + c.end)
    print('green', c.green + "hello" + c.end)
    print('orange', c.orange + "hello" + c.end)
    print('yellow', c.yellow + "hello" + c.end)
    print('white', c.white + "hello" + c.end)

    print('bgBlack', c.bgBlack + "Hello" + c.end)
    print('bgBlue', c.bgBlue + "Hello" + c.end)
    print('bgRed', c.bgRed + "Hello" + c.end)
    print('bgGreen', c.bgGreen + "Hello" + c.end)
    print('bgOrange', c.bgOrange + "Hello" + c.end)
    print('bgYellow', c.bgYellow + "Hello" + c.end)
    print('bgWhite', c.bgWhite + "Hello" + c.end)

    print('bold', c.bold + "Hello" + c.end)
    print('underline', c.underline + "Hello" + c.end)
    print('blink', c.blink + "Hello" + c.end)
    print('inverse', c.inverse + "Hello" + c.end)
    print('hidden', c.hidden + "Hello" + c.end)


    print('combo 1', c.bgRed + c.hidden + "Hello" + c.end)
    print('combo 2', c.green + c.blink + c.bgYellow + "Hello" + c.end)
    print('combo 3', c.bgBlue + "  " + c.bgWhite + "  " + c.bgRed + "  " + c.end)

