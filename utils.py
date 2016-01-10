import numpy as np
import sys
from os import name as os_name
import subprocess
import getopt
import itertools


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

def readArgs():
    """
    readArgs

    Lecture des arguments passés au script, version avancée.
    En particulier, on veut lire --cube=<cube à résoudre>
    ou -c=<cube à résoudre>

    :Returns:
        {Dict}      {cube: <cube à résoudre>} uniquement pour l'instant
    """
    result = {}

    optlist, args = getopt.getopt(
        sys.argv[1:],
        'c:s:taC',
        ['cube=',
        'speed=',
        'tuto',
        'auto',
        'colors']
    )

    arguments = {k: v for k, v in optlist} #on tranforme la list en dict

    if '-c' in arguments:
        result['cube'] = arguments['-c']

    if '--cube' in arguments:
        result['cube'] = arguments['--cube'] #--cube override -c

    if '-s' in arguments:
        result['speed'] = arguments['-s']

    if '--speed' in arguments:
        result['speed'] = arguments['--speed'] #--speed override -s

    if '-t' in arguments:
        result['tuto'] = arguments['-t']

    if '--tuto' in arguments:
        result['tuto'] = arguments['--tuto'] #--tuto override -t

    if '-a' in arguments:
        result['auto'] = arguments['-a']

    if '--auto' in arguments:
        result['auto'] = arguments['--auto'] #--auto override -a

    if '-C' in arguments:
        result['colors'] = arguments['-C']

    if '--colors' in arguments:
        result['colors'] = arguments['--colors'] #--colors override -C

    return result

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
        space   {Boolean}

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
params = readArgs()
if os_name == 'nt' and not 'colors' in params:
    TermColors = winTermColors()
else:
    TermColors = unixTermColors()

def croix_valide(c):
    """
    croix_valide

    Détermine si le cube `c` est bien passé à par l'étape 1 du CFOP
    ie. que la croix est formée

    :Args:
        c   {Cube}

    :Returns:
        {Boolean}
    """
    croixBlanche = (
        c.get_facette('FD', 0),
        c.get_facette('FD', 1),
        c.get_facette('RD', 0),
        c.get_facette('RD', 1),
        c.get_facette('BD', 0),
        c.get_facette('BD', 1),
        c.get_facette('LD', 0),
        c.get_facette('LD', 1)
    )

    return croixBlanche == (1, 0, 2, 0, 3, 0, 4, 0)

def ftl_valide(c):
    """
    ftl_valide

    Détermine si le cube `c` est bien passé par l'étape 2 du CFOP
    ie. que les deux premières couronnes sont ok

    :Args:
        c   {Cube}

    :Returns:
        {Boolean}
    """

    facettes = (
        c.get_facette('RBD', 2), #coins de Down
        c.get_facette('BLD', 2),
        c.get_facette('FRD', 2),
        c.get_facette('LFD', 2),

        c.get_facette('RBD', 1),
        c.get_facette('RBD', 0),

        c.get_facette('BLD', 1),
        c.get_facette('BLD', 0),

        c.get_facette('FRD', 1),
        c.get_facette('FRD', 0),

        c.get_facette('LFD', 1),
        c.get_facette('LFD', 0),

        c.get_facette('FL', 0), #couronnes
        c.get_facette('FL', 1),

        c.get_facette('FR', 0),
        c.get_facette('FR', 1),

        c.get_facette('BL', 0),
        c.get_facette('BL', 1),

        c.get_facette('BR', 0),
        c.get_facette('BR', 1),

    )

    valide = (
        0, #coins de la face blanche
        0,
        0,
        0,

        3,
        2,
        4,
        3,

        2,
        1,

        1,
        4,

        1, #couronnes
        4,

        1,
        2,

        3,
        4,

        3,
        2
    )

    return  facettes == valide

def cfop_valide(cube, mouvements):
    """
    cfop_valide

    :Returns:
        {Boolean}   True si la suite de mouvements appliquée sur cube
                    donne bien un cube résolu
    """
    cube.mouvements(mouvements)
    return cube.resolu()

def translate_mvt(mvt):
    """
    translate_mvt

    Traduit les mouvements inverses *i en *'

    :Args:
        mvt   {String}

    :Returns:
        {String}
    """
    if len(mvt) > 1 and mvt[1]=="i" :
        mvt = mvt[0] + "'"
    return mvt

def clear():
    """
    clear

    Clear terminal screen
    Voir : http://stackoverflow.com/a/1433135/2058840
    """

    if os_name == 'nt':
        subprocess.call("cls", shell=True) # windows, attention ne marche pas sur gitbash
    else:
        subprocess.call("clear") # linux/mac

def newGetch():
    """
    newGetch

    Ecoute le premier caractère saisi par l'user
    Voir : http://code.activestate.com/recipes/134892/
    """

    if os_name == 'nt':  # windows
        from msvcrt import getch
        return getch()

    else:  # linux/mac
        import tty, termios

        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

def find_sublists(seq, sublist):
    """
    find_sublists

    Recherche d'une sous-liste dans une liste

    :Args:
        seq     {List}  La liste complète
        sublist {List}  La sous-liste qu'on recherche dans seq

    :Returns:
        {Generator}     Ca retourner ({Int}, {Int}) : positions début/fin
                        des sous-listes trouvées dans seq si il y en a

    :Source:
        Copier/Coller de http://stackoverflow.com/a/12898180/2058840
        Ajout des commentaires

        Voir http://stackoverflow.com/a/231855/2058840 pour explications
        sur les générateurs et yield
    """
    length = len(sublist) #taille de la sous liste recherchée
    for index, value in enumerate(seq):
        #quand on a trouvé la sublist dans seq
        #(ie. à la position [index:index + length])
        #on yield sa position
        #si plusieurs match, on yieldera la prochaine position au prochain appel
        if value == sublist[0] and seq[index:index+length] == sublist:
            yield index, index+length

def replace_sublist(seq, target, replacement):
    """
    replace_sublist

    Remplacement de la sous-liste `target` de `seq` par `replacement`

    :Args:
        seq         {List}  La liste complète
        target      {List}  La sous-liste qu'on recherche dans seq
        replacement {List}  La sous-liste qui va remplacer target

    :Source:
        Copier/Coller de http://stackoverflow.com/a/12898180/2058840
        Ajout des commentaires

        Voir http://stackoverflow.com/a/231855/2058840 pour explications
        sur les générateurs et yield
    """
    #on récupère un générateurs des emplacements de target dans seq
    sublists = find_sublists(seq, target)
    #pour chaque emplacement, on remplace
    for start, end in sublists:
        seq[start:end] = replacement

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

    a = [1, 2, 6, 7, 8, 4]
    replace_sublist(a, [6, 7, 8], [3])
    print(a)

