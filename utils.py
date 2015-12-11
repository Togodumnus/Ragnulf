import numpy as np
import sys
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

def colorize(c, convert=None):
    """
    colorize

    :Args:
        c       {String}    La couleur (W, B, R, G, O, Y)
        convert {List}      Optionel. Une traduction.
                            ex: convert[0] = <la traduction de W>, etc.
                            Defaut, voir COULEURS

    :Returns:
        {String}        Une chaîne prête à être renvoyée au terminal pour un
                        affichage coloré
    """

    if not convert:
        convert = COULEURS

    if c == 'W':
        return TermColors.bgWhite + TermColors.black + convert[0] + TermColors.end
    elif c == 'B':
        return TermColors.bgBlue + convert[1] + TermColors.end
    elif c == 'R':
        return TermColors.bgRed + convert[2] + TermColors.end
    elif c == 'G':
        return TermColors.bgGreen + convert[3] + TermColors.end
    elif c == 'O':
        return TermColors.bgOrange + convert[4] + TermColors.end
    elif c == 'Y':
        return TermColors.bgYellow + TermColors.black + convert[5] + TermColors.end
    else:
        return c

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

    black  = ''
    blue   = ''
    red    = ''
    green  = ''
    orange = ''
    yellow = ''
    white  = ''

    bgBlack  = ''
    bgBlue   = ''
    bgRed    = ''
    bgGreen  = ''
    bgOrange = ''
    bgYellow = ''
    bgWhite  = ''

    bold      = ''
    underline = ''
    blink     = ''
    inverse   = ''
    hidden    = ''

    end = ''

    def __init__(self):
        pass

#Windows n'aime pas trop les couleurs ascii
if os_name == 'nt' and not '--colors' in sys.argv:
    TermColors = winTermColors()
else:
    TermColors = unixTermColors()

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

    print("Test colorize")
    print("Red", colorize('R'))

