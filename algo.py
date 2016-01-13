'''
Algo de résolution
-----------------

Pour cet algo, on va utiliser la méthode CFOP décrite dans cette vidéo :
https://www.youtube.com/watch?v=VwvGWNfcgs8

Fridrich method [CFOP]

--> Cross
http://www.youtube.com/watch?v=WzE7SyDB8vA

--> First Two Layers
http://www.youtube.com/watch?v=IT5BPHEZGJE


--> Orienting Last Layer
http://www.youtube.com/watch?v=q5ltbjGIosU

--> Permuting last Layer
http://www.youtube.com/watch?v=IMb7hOAgmng

Utile : mouvementsr de rubiks :
----------------------------
http://ruwix.com/puzzle-mouvements-generator/

'''

from Cube import Cube
from lire_entree import lecture_cube
from utils import croix_valide, ftl_valide, cfop_valide
from test import tableaux_test



def algo_cfop(c):
    '''
    algo

    Prend le cube en entrée, et avec l'algo de résolution choisi,
    va déterminer la suite de mouvements qu'il faut réaliser pour résoudre le cube

    :Args:
        c {Cube}    l'objet cube, à résoudre

    :Returns:
        {None|String}, {None|String}
                    Si le cube ne peut pas être résolu, renverra False
                    sinon, renverra une liste de String correspondant aux
                    différents mouvements à effectuer pour résoudre le cube
    '''

    face_resolue = lambda x: x.face_resolu('U')
    resolu = lambda x: x.resolu()
    noop = lambda x: (x, ())

    cube, mouv = cross_facile(c) #on commence par la croix

    #on continue en vérifiant l'état précédant à chaque étape
    for (k, f) in ( #après vérification de chaque condition k
                    #appliquer la fonction f
            (croix_valide, ftl),
            (ftl_valide,   oll),
            (face_resolue, pll),
            (resolu,       noop)
        ):
        if k(cube):
            cube, tmp = f(c)
            mouv += tmp
        else:
            return "Le cube est insolvable", None

    return None, mouv

def cross_facile(c):
    '''
    cross_facile

    Etape 1 de l'algo CFOP
    ----------------------
    Prend le cube en entrée et réalise la première étape de l'algo CFOP
    c'est à dire réalise une croix sur la face blanche et fait en sorte d'avoir
    2 couleurs identiques à chaque extremités de la croix, exemple :

               Y  G  Y
               R  Y  Y
               W  G  B
     R  B  G   R  R  O   W  R  G   O  O  B
     B  O  Y   G  B  O   Y  R  B   Y  G  O
     Y  O  O   W  B  W   B  R  G   R  G  O
               G  W  R
               W  W  W
               B  W  Y

    Sources
    -------
    - https://www.youtube.com/watch?feature=player_detailpage&v=WzE7SyDB8vA
        "THE ADVANCED CROSS"
    - francocube
        http://forum.francocube.com/viewtopic.php?t=5464
        Il précise sur ce forum que pour réaliser une croix,
        c'est 8 mouvements maximum, et 7 dans la majorité des cas.

    :Args:
        c           {Cube}      L'objet cube, à résoudre
        mouvements  {String}    Liste des mouvements à réalisé qui sera complété au fur
                                      et à mesure des étapes de l'algo

    :Returns:
        {Cube}, {Tupple}        L'objet cube avec la croix blanche faite
                                Liste des mouvements à faire
    '''

    mouvementsTemp = () #liste des mouvements à effectués pour avancer dans l'algo
    mouvementsTotal = ()

    #On veut mettre l'arrête bleue-blanche à côté de la pièce centrale blanche
    #ie. la placer en FB jsute en dessous la pièce centrale bleue

    #On cherche l'arête bleue blanche
    if c.cube_contient_couleur('FU', 0, 1): #Si elle est sur la première couronne
        mouvementsTemp = ('F2',)
    elif c.cube_contient_couleur('RU', 0, 1):
        mouvementsTemp = ('U', 'F2')
    elif c.cube_contient_couleur('BU', 0, 1):
        mouvementsTemp = ('U2', 'F2')
    elif c.cube_contient_couleur('LU', 0, 1):
        mouvementsTemp = ('Ui', 'F2')

    elif c.cube_contient_couleur('FR', 0, 1): #Deuxième couronne
        mouvementsTemp = ('R', 'U', 'F2')
    elif c.cube_contient_couleur('BR', 0, 1):
        mouvementsTemp = ('Ri', 'U', 'F2')
    elif c.cube_contient_couleur('BL', 0, 1):
        mouvementsTemp = ('Bi', 'U2', 'F2')
    elif c.cube_contient_couleur('FL', 0, 1):
        mouvementsTemp = ('Fi',)

    elif c.cube_contient_couleur('LD', 0, 1): #Troisième couronne, autour du blanc
        mouvementsTemp = ('L2', 'Ui', 'F2')
    elif c.cube_contient_couleur('RD', 0, 1):
        mouvementsTemp = ('R2', 'U', 'F2')
    elif c.cube_contient_couleur('BD', 0, 1):
        mouvementsTemp = ('B2', 'U2', 'F2')

    if len(mouvementsTemp) > 0:
        c.mouvements(mouvementsTemp) #on effectue les mouvements
        mouvementsTotal += mouvementsTemp
        mouvementsTemp = ()

    #À ce niveau là, l'arrête bleue-blanche est au niveau de la troisième couronne
    #à l'endroit où il faut mais pas forcément paramétré comme il le faut: WWBB et pas WBWB

    if c.get_facette('FD', 0) != 1 : #Si pas bien paramétré, il y a une suite de mouvements à effectuer
        mouvementsTemp = ('Fi', 'B', 'Ri', 'Di')
        c.mouvements(mouvementsTemp)
        mouvementsTotal += mouvementsTemp
        mouvementsTemp = ()

    #La partie blanc-bleue est complétée

    #On fait pareil pour la partie orange

    if c.cube_contient_couleur('FU', 0, 4): #Si elle est sur la première couronne
        mouvementsTemp = ('U', 'L2')
    elif c.cube_contient_couleur('RU', 0, 4):
        mouvementsTemp = ('U2', 'L2')
    elif c.cube_contient_couleur('BU', 0, 4):
        mouvementsTemp = ('Ui', 'L2')
    elif c.cube_contient_couleur('LU', 0, 4):
        mouvementsTemp = ('L2',)

    elif c.cube_contient_couleur('FR', 0, 4): #Deuxième couronne
        mouvementsTemp = ('R', 'U2', 'L2')
    elif c.cube_contient_couleur('BR', 0, 4):
        mouvementsTemp = ('B', 'Ui', 'L2')
    elif c.cube_contient_couleur('BL', 0, 4):
        mouvementsTemp = ('Li',)
    elif c.cube_contient_couleur('FL', 0, 4):
        mouvementsTemp = ('L',)

    elif c.cube_contient_couleur('RD', 0, 4): #Troisième couronne, autour du blanc
        mouvementsTemp = ('R2', 'U2', 'L2')
    elif c.cube_contient_couleur('BD', 0, 4):
        mouvementsTemp = ('B2', 'Ui', 'L2')

    if len(mouvementsTemp) > 0:
        c.mouvements(mouvementsTemp) #on effectue les mouvements
        mouvementsTotal += mouvementsTemp
        mouvementsTemp = ()

    #A ce niveau là, l'arrête orange blanche est au niveau de la troisième couronne
    #à l'endroit où il faut mais pas forcément paramétré comme il le faut : WWOO et pas WOWO

    if c.get_facette('LD', 0) != 4 : #Si pas bien paramétré,
                                     #il y a une suite de mouvements à effectuer
        mouvementsTemp = ('Li', 'D', 'Fi', 'Di')
        c.mouvements(mouvementsTemp)
        mouvementsTotal += mouvementsTemp
        mouvementsTemp = ()

    #La partie orange est complétée

    #On fait pareil pour la partie verte

    if c.cube_contient_couleur('FU', 0 ,3): #Si elle est sur la première couronne
        mouvementsTemp = ('U2', 'B2')
    elif c.cube_contient_couleur('RU', 0 ,3):
        mouvementsTemp = ('Ui', 'B2')
    elif c.cube_contient_couleur('BU', 0 ,3):
        mouvementsTemp = ('B2',)
    elif c.cube_contient_couleur('LU', 0 ,3):
        mouvementsTemp = ('U', 'B2')

    elif c.cube_contient_couleur('FR', 0 ,3): #Deuxième couronne
        mouvementsTemp = ('R', 'Ui', 'B2')
    elif c.cube_contient_couleur('BL', 0 ,3):
        mouvementsTemp = ('B',)
    elif c.cube_contient_couleur('BR', 0 ,3):
        mouvementsTemp = ('Bi',)
    elif c.cube_contient_couleur('FL', 0 ,3):
        mouvementsTemp = (
            'Li', 'U',
            'L', # Pour remettre la partie d'avant à sa place
            'B2'
        )

    elif c.cube_contient_couleur('RD', 0 ,3): #Troisième couronne, autour du blanc
        mouvementsTemp = ('R2', 'Ui', 'B2')

    if len(mouvementsTemp) > 0:
        c.mouvements(mouvementsTemp) #on effectue les mouvements
        mouvementsTotal += mouvementsTemp
        mouvementsTemp = ()

    #À ce niveau là, l'arrête verte blanche est au niveau de la troisième couronne
    #à l'endroit où il faut mais pas forcément paramétré comme il le faut : WWGG et pas WGWG

    if c.get_facette('BD', 0) != 3 : #Si pas bien paramétré,
                                     #il y a une suite de mouvements à effectuer
        mouvementsTemp = ('Bi', 'D', 'Li', 'Di')
        c.mouvements(mouvementsTemp)
        mouvementsTotal += mouvementsTemp
        mouvementsTemp = ()

    #La partie verte est complétée

    #On fait pareil pour la partie rouge

    if c.cube_contient_couleur('FU', 0 ,2): #Si elle est sur la première couronne
        mouvementsTemp = ('Ui', 'R2')
    elif c.cube_contient_couleur('RU', 0 ,2):
        mouvementsTemp = ('R2',)
    elif c.cube_contient_couleur('BU', 0 ,2):
        mouvementsTemp = ('U', 'R2')
    elif c.cube_contient_couleur('LU', 0 ,2):
        mouvementsTemp = ('U2', 'R2')

    elif c.cube_contient_couleur('FR', 0 ,2): #Deuxième couronne
        mouvementsTemp = ('Ri',)
    elif c.cube_contient_couleur('BL', 0 ,2):
        mouvementsTemp = (
            'Bi', 'U',
            'B', # Pour remettre la partie d'avant à sa place
            'R2'
        )

    elif c.cube_contient_couleur('BR', 0 ,2):
        mouvementsTemp = ('R',)
    elif c.cube_contient_couleur('FL', 0 ,2):
        mouvementsTemp = ('F', 'Ui', 'Fi', 'R2')

    if len(mouvementsTemp) > 0:
        c.mouvements(mouvementsTemp) #on effectue les mouvements
        mouvementsTotal += mouvementsTemp
        mouvementsTemp = ()

    #A ce niveau là, l'arrête rouge blanche est au niveau de la troisième couronne
    #à l'endroit où il faut mais pas forcément paramétré comme il le faut : WWRR et pas WOWR

    if c.get_facette('RD', 0) != 2 : #Si pas bien paramétré,
                                     #il y a une suite de mouvements à effectuer
        mouvementsTemp = ('Ri', 'D', 'Bi', 'Di')
        c.mouvements(mouvementsTemp)
        mouvementsTotal += mouvementsTemp
        mouvementsTemp = ()


    return c, mouvementsTotal

def ftl(c):
    '''
    Etape 2 de l'algo CFOP
    Faire les deux "layers", c'est à dire avoir les côtés
    Vert, Rouge, Bleu et Orange au 2/3 fais, exemple :
           W W W
           W W W
           W W W
    O O O  G G G  R R R  B B B
    O O O  G G G  R R R  B B B
    X X X  X X X  X X X  X X X
           X X X
           X X X
           X X X

    :Args:
    c {Cube}, mouvements {String} l'objet cube, à résoudre

    :Returns:
    {Cube}, {String} L'objet cube avec les deux layers de faite
                    Liste des mouvements à faire
    '''
    # La méthode optimisé pour résoudre FTL consiste à inseré les deux cubes en même temps
    mouvementsTotal = () # mouvements total, ce qui vas etre renvoyé
    mouvementsTemp = () # liste de mouvements qui vas etre executé pour avancé dans l'algo

    # Insertion de la pair Bleu Rouge
    # Deplacé le cube si il est placé en BR ou BL ou FL
    if c.cube_contient_couleur('BR',1,2):
        mouvementsTemp = ('Ri','U','R')
    elif c.cube_contient_couleur('BL',1,2):
        mouvementsTemp = ('L','U','Li')
    elif c.cube_contient_couleur('FL',1,2):
        mouvementsTemp = ('Li','U','L')

    if len(mouvementsTemp) > 0:
        c.mouvements(mouvementsTemp) #on effectue les mouvements
        mouvementsTotal += mouvementsTemp
        mouvementsTemp = ()

    # Le cube doit etre en FRU ou FRD
    if c.cube_contient_couleur('LFU',0,1,2):
        mouvementsTemp = ('Ui',)
    elif c.cube_contient_couleur('BLU',0,1,2):
        mouvementsTemp = ('U2',)
    elif c.cube_contient_couleur('RBU',0,1,2):
        mouvementsTemp = ('U',)
    else: # cube en down : chaque cas doit être traité séparement
          # en fonction de où est le cube bleu rouge
        if c.cube_contient_couleur('LU',1,2): # à gauche
            if c.cube_contient_couleur('LFD',0,1,2):
                mouvementsTemp = ('Ui','Li','Ui','L')
            elif c.cube_contient_couleur('RBD',0,1,2):
                mouvementsTemp = ('Ri','Ui','R','U2')
            elif c.cube_contient_couleur('BLD',0,1,2):
                mouvementsTemp = ('U','L','U2','Li')
        elif c.cube_contient_couleur('RU',1,2): # à droite
            if c.cube_contient_couleur('LFD',0,1,2):
                mouvementsTemp = ('Li','Ui','L')
            elif c.cube_contient_couleur('RBD',0,1,2):
                mouvementsTemp = ('Ri','Ui','R','U2')
            elif c.cube_contient_couleur('BLD',0,1,2):
                mouvementsTemp = ('L','U','Li','U')
        elif c.cube_contient_couleur('BU',1,2): # cube derrière
            if c.cube_contient_couleur('LFD',0,1,2):
                mouvementsTemp = ('Li','U2','L','U')
            elif c.cube_contient_couleur('RBD',0,1,2):
                mouvementsTemp = ('Ri','Ui','R','U2')
            elif c.cube_contient_couleur('BLD',0,1,2):
                mouvementsTemp = ('L','U2','Li')
        elif c.cube_contient_couleur('FU',1,2): # devant
            if c.cube_contient_couleur('LFD',0,1,2):
                mouvementsTemp = ('Li','Ui','L')
            elif c.cube_contient_couleur('RBD',0,1,2):
                mouvementsTemp = ('Ri','U2','R','Ui')
            elif c.cube_contient_couleur('BLD',0,1,2):
                mouvementsTemp = ('L','U2','Li')
        elif c.cube_contient_couleur('FR',1,2): # bien placé
            if c.cube_contient_couleur('LFD',0,1,2):
                mouvementsTemp = ('Li','Ui','L')
            elif c.cube_contient_couleur('RBD',0,1,2):
                mouvementsTemp = ('Ri','U2','R','Ui')
            elif c.cube_contient_couleur('BLD',0,1,2):
                mouvementsTemp = ('L','U2','Li')

    if len(mouvementsTemp) > 0:
        c.mouvements(mouvementsTemp) #on effectue les movements
        mouvementsTotal += mouvementsTemp
        mouvementsTemp = ()

    if c.cube_contient_couleur('FRU',0,1,2): # cube bleu rouge blanc en FRU
        if c.get_facette('FRU',2)==0: # face blanche en haut
            if c.cube_contient_couleur('FR',1,2): # cube bleu rouge en FR
                if c.get_facette('FR',0)==1: # bleu en front
                    mouvementsTemp = ('R','U','Ri','Ui','R','U','Ri','Ui','R','U','Ri')
                elif c.get_facette('FR',0)==2: # rouge en front
                    mouvementsTemp = ('R','Ui','Ri','U','Fi','U','F')
            elif c.cube_contient_couleur('LU',1,2): # cube bleu rouge en  LU
                if c.get_facette('LU',1)==1: # bleu en haut
                    mouvementsTemp = ('U2','R','U','Ri','U','R','Ui','Ri')
                elif c.get_facette('LU',1)==2: # rouge en haut
                    mouvementsTemp = ('Ui','Fi','U2','F','Ui','Fi','U','F') # a faire
            elif c.cube_contient_couleur('FU',1,2):
                if c.get_facette('FU',1)==1: # bleu up
                    mouvementsTemp = ('R','U','Ri','U2','R','U','Ri','Ui','R','U','Ri')
                if c.get_facette('FU',1)==2:
                    mouvementsTemp = ('Fi','U2','F','U','Fi','Ui','F')
            elif c.cube_contient_couleur('RU',1,2):
                if c.get_facette('RU',1)==1:
                    mouvementsTemp = ('R','U2','Ri','Ui','R','U','Ri')
                if c.get_facette('RU',1)==2:
                    mouvementsTemp = ('Fi','Ui','F','U2','Fi','Ui','F','U','Fi','Ui','F')
            elif c.cube_contient_couleur('BU',1,2):
                if c.get_facette('BU',1)==1:
                    mouvementsTemp = ('U','R','U2','Ri','U','R','Ui','Ri')
                if c.get_facette('BU',1)==2:
                    mouvementsTemp = ('U2','Fi','Ui','F','Ui','Fi','U','F')
        elif c.get_facette('FRU',2)==1: # face bleu en haut
            if c.cube_contient_couleur('FR',1,2): # cube bleu rouge en FR
                if c.get_facette('FR',0)==1: # bleu en front
                    mouvementsTemp = ('Ui','R','Ui','Ri','Ui','R','U2','Ri')
                elif c.get_facette('FR',0)==2: # rouge en front
                    mouvementsTemp = ('Ui','R','U','Ri','U','Fi','Ui','F')
            elif c.cube_contient_couleur('LU',1,2): # cube bleu rouge en  LU
                if c.get_facette('LU',1)==1: # bleu en haut
                    mouvementsTemp = ('Ui','R','U2','Ri','Ui','R','U2','Ri')
                elif c.get_facette('LU',1)==2: # rouge en haut
                    mouvementsTemp = ('Fi','Ui','F')
            elif c.cube_contient_couleur('FU',1,2):
                if c.get_facette('FU',1)==1: # bleu up
                    mouvementsTemp =  ('Fi','U','F','U2','R','U','Ri')
                if c.get_facette('FU',1)==2: # rouge up
                    mouvementsTemp = ('U','Fi','U','F','Ui','Fi','Ui','F')
            elif c.cube_contient_couleur('RU',1,2):
                if c.get_facette('RU',1)==1:
                    mouvementsTemp = ('U','R','Ui','Ri')
                if c.get_facette('RU',1)==2:
                    mouvementsTemp = ('Ui','R','U2','Ri','U','Fi','Ui','F')
            elif c.cube_contient_couleur('BU',1,2):
                if c.get_facette('BU',1)==1:
                    mouvementsTemp = ('Ui','R','U','Ri','Ui','R','U2','Ri')
                if c.get_facette('BU',1)==2:
                    mouvementsTemp = ('U','Fi','Ui','F','Ui','Fi','Ui','F')
        elif c.get_facette('FRU',2)==2: # rouge en haut
            if c.cube_contient_couleur('FR',1,2): # cube bleu rouge en FD
                if c.get_facette('FR',0)==1: # bleu en front
                    mouvementsTemp = ('U','Fi','U','F','U','Fi','U2','F')
                elif c.get_facette('FR',0)==2: # rouge en front
                    mouvementsTemp = ('U','Fi','Ui','F','Ui','R','U','Ri')
            elif c.cube_contient_couleur('LU',1,2): # cube bleu rouge en  LU
                if c.get_facette('LU',1)==1: # bleu en haut
                    mouvementsTemp = ('Ui','R','U','Ri','U','R','U','Ri')
                elif c.get_facette('LU',1)==2: # rouge en haut
                    mouvementsTemp = ('U','Fi','Ui','F','U','Fi','U2','F')
            elif c.cube_contient_couleur('FU',1,2):
                if c.get_facette('FU',1)==1: # bleu up
                    mouvementsTemp = ('U','Fi','U2','F','Ui','R','U','Ri')
                if c.get_facette('FU',1)==2: # rouge up
                    mouvementsTemp = ('Ui','Fi','U','F')
            elif c.cube_contient_couleur('RU',1,2):
                if c.get_facette('RU',1)==1:
                    mouvementsTemp = ('Ui','R','Ui','Ri','U','R','U','Ri')
                if c.get_facette('RU',1)==2:
                    mouvementsTemp = ('R','Ui','Ri','U2','Fi','Ui','F')
            elif c.cube_contient_couleur('BU',1,2):
                if c.get_facette('BU',1)==1:
                    mouvementsTemp = ('R','U','Ri')
                if c.get_facette('BU',1)==2:
                    mouvementsTemp = ('U','Fi','U2','F','U','Fi','U2','F')

    elif c.cube_contient_couleur('FRD',0,1,2):
        if c.get_facette('FRD',0)==0: # face blanche en front
            if c.cube_contient_couleur('FR',1,2): # cube bleu rouge en FD
                if c.get_facette('FR',0)==1: # bleu en front
                    mouvementsTemp = ('R','Ui','Ri','Ui','R','U','Ri','Ui','R','U2','Ri')
                elif c.get_facette('FR',0)==2: # rouge en front
                    mouvementsTemp = ('R','Ui','Ri','U','Fi','Ui','F','Ui','Fi','Ui','F')
            elif c.cube_contient_couleur('LU',1,2): # cube bleu rouge en  LU
                if c.get_facette('LU',1)==1: # bleu en haut
                    mouvementsTemp = ('U2','R','Ui','Ri','U','R','Ui','Ri')
                elif c.get_facette('LU',1)==2: # rouge en haut
                    mouvementsTemp = ('Ui','Fi','Ui','F','U','Fi','Ui','F')
            elif c.cube_contient_couleur('FU',1,2):
                if c.get_facette('FU',1)==1: # bleu up
                    mouvementsTemp = ('Ui','R','Ui','Ri','U','R','Ui','Ri')
                if c.get_facette('FU',1)==2:
                    mouvementsTemp = ('Fi','Ui','F','U','Fi','Ui','F')
            elif c.cube_contient_couleur('RU',1,2):
                if c.get_facette('RU',1)==1:
                    mouvementsTemp = ('R','Ui','Ri','U','R','Ui','Ri')
                if c.get_facette('RU',1)==2:
                    mouvementsTemp = ('U','Fi','Ui','F','U','Fi','Ui','F')
            elif c.cube_contient_couleur('BU',1,2):
                if c.get_facette('BU',1)==1:
                    mouvementsTemp = ('U','R','Ui','Ri','U','R','Ui','Ri')
                if c.get_facette('BU',1)==2:
                    mouvementsTemp = ('U2','Fi','Ui','F','U','Fi','Ui','F')
        elif c.get_facette('FRD',0)==1: # face bleu en front
            if c.cube_contient_couleur('FR',1,2): # cube bleu rouge en FR
                if c.get_facette('FR',0)==1: # bleu en front
                    pass # déjà bien placé
                elif c.get_facette('FR',0)==2: # rouge en front
                    mouvementsTemp = ('R','Ui','Ri','U','Fi','U2','F','U','Fi','U2','F')
            elif c.cube_contient_couleur('LU',1,2): # cube bleu rouge en  LU
                if c.get_facette('LU',1)==1: # bleu en haut
                    mouvementsTemp = ('U','Fi','U','F','U','R','Ui','Ri')
                elif c.get_facette('LU',1)==2: # rouge en haut
                    mouvementsTemp = ('R','Ui','Ri','Ui','Fi','U','F')
            elif c.cube_contient_couleur('FU',1,2):
                if c.get_facette('FU',1)==1: # bleu up
                    mouvementsTemp = ('U2','Fi','U','F','U','R','Ui','Ri')
                if c.get_facette('FU',1)==2: # rouge up
                    mouvementsTemp = ('U','R','Ui','Ri','Ui','Fi','U','F')
            elif c.cube_contient_couleur('RU',1,2):
                if c.get_facette('RU',1)==1:
                    mouvementsTemp = ('Ui','Fi','U','F','U','R','Ui','Ri')
                if c.get_facette('RU',1)==2:
                    mouvementsTemp = ('U2','R','Ui','Ri','Ui','Fi','U','F')
            elif c.cube_contient_couleur('BU',1,2):
                if c.get_facette('BU',1)==1:
                    mouvementsTemp = ('Fi','U','F','U','R','Ui','Ri')
                if c.get_facette('BU',1)==2:
                    mouvementsTemp = ('Ui','R','Ui','Ri','Ui','Fi','U','F')
        elif c.get_facette('FRD',0)==2: # rouge en front
            if c.cube_contient_couleur('FR',1,2): # cube bleu rouge en FR
                if c.get_facette('FR',0)==1: # bleu en front
                    mouvementsTemp = ('R','Ui','Ri','U','R','U2','Ri','U','R','Ui','Ri')
                elif c.get_facette('FR',0)==2: # rouge en front
                    mouvementsTemp = ('R','U','Ri','Ui','R','Ui','Ri','U2','Fi','Ui','F')
            elif c.cube_contient_couleur('LU',1,2): # cube bleu rouge en  LU
                if c.get_facette('LU',1)==1: # bleu en haut
                    mouvementsTemp = ('U2','R','U','Ri','Ui','R','U','Ri')
                elif c.get_facette('LU',1)==2: # rouge en haut
                    mouvementsTemp = ('Ui','Fi','U','F','Ui','Fi','U','F')
            elif c.cube_contient_couleur('FU',1,2):
                if c.get_facette('FU',1)==1: # bleu up
                    mouvementsTemp = ('Ui','R','U','Ri','Ui','R','U','Ri')
                if c.get_facette('FU',1)==2: # rouge up
                    mouvementsTemp = ('Fi','U','F','Ui','Fi','U','F')
            elif c.cube_contient_couleur('RU',1,2):
                if c.get_facette('RU',1)==1:
                    mouvementsTemp = ('R','U','Ri','Ui','R','U','Ri')
                if c.get_facette('RU',1)==2:
                    mouvementsTemp = ('U','Fi','U','F','Ui','Fi','U','F')
            elif c.cube_contient_couleur('BU',1,2):
                if c.get_facette('BU',1)==1:
                    mouvementsTemp = ('U','R','U','Ri','Ui','R','U','Ri')
                if c.get_facette('BU',1)==2:
                    mouvementsTemp = ('U2','Fi','U','F','Ui','Fi','U','F')

    if len(mouvementsTemp) > 0:
        c.mouvements(mouvementsTemp) #on effectue les mouvements
        mouvementsTotal += mouvementsTemp
        mouvementsTemp = ()

    # Insertion de la pair Vert Rouge
    # Deplacer le cube si il est placé en BR ou BL ou FL
    if c.cube_contient_couleur('BL',2,3):
        mouvementsTemp = ('L','U','Li')
    elif c.cube_contient_couleur('FL',2,3):
        mouvementsTemp = ('Li','U','L')

    if len(mouvementsTemp) > 0:
        c.mouvements(mouvementsTemp) #on effectue les mouvements
        mouvementsTotal += mouvementsTemp
        mouvementsTemp = ()

    # Le cube doit etre en LBU ou BLD
    if c.cube_contient_couleur('LFU',0,2,3):
        mouvementsTemp = ('U2',)
    elif c.cube_contient_couleur('BLU',0,2,3):
        mouvementsTemp = ('U',)
    elif c.cube_contient_couleur('FRU',0,2,3):
        mouvementsTemp = ('Ui',)
    else: # cube en down : chaque cas doit être traité separement
          # en fonction de où est le cube bleu rouge
        if c.cube_contient_couleur('LU',2,3): # à gauche
            if c.cube_contient_couleur('LFD',0,2,3):
                mouvementsTemp = ('U','Li','U2','L')
            elif c.cube_contient_couleur('BLD',0,2,3):
                mouvementsTemp = ('U','L','U','Li')
        elif c.cube_contient_couleur('RU',2,3): # à droite
            if c.cube_contient_couleur('LFD',0,2,3):
                mouvementsTemp = ('Li','Ui','L','Ui')
            elif c.cube_contient_couleur('BLD',0,2,3):
                mouvementsTemp = ('L','U','Li')
        elif c.cube_contient_couleur('BU',2,3): # cube derrière
            if c.cube_contient_couleur('LFD',0,2,3):
                mouvementsTemp = ('Li','U2','L')
            elif c.cube_contient_couleur('BLD',0,2,3):
                mouvementsTemp = ('L','U','Li')
        elif c.cube_contient_couleur('FU',2,3): # devant
            if c.cube_contient_couleur('LFD',0,2,3):
                mouvementsTemp = ('Li','U2','L')
            elif c.cube_contient_couleur('BLD',0,2,3):
                mouvementsTemp = ('L','U2','Li','Ui')
        elif c.cube_contient_couleur('BR',2,3): # bien placé
            if c.cube_contient_couleur('LFD',0,2,3):
               mouvementsTemp = ('Li','U2','L')
            elif c.cube_contient_couleur('BLD',0,2,3):
                mouvementsTemp = ('L','U','Li')

    if len(mouvementsTemp) > 0:
        c.mouvements(mouvementsTemp) #on effectue les mouvements
        mouvementsTotal += mouvementsTemp
        mouvementsTemp = ()

    if c.cube_contient_couleur('RBU',0,2,3): # cube bleu rouge blanc en RBU
        if c.get_facette('RBU',2)==0: # face blanche en haut
            if c.cube_contient_couleur('BR',2,3): # cube bleu rouge en BR
                if c.get_facette('BR',1)==2: # bleu en BRont
                    mouvementsTemp = ('B','U','Bi','Ui','B','U','Bi','Ui','B','U','Bi')
                elif c.get_facette('BR',1)==3: # rouge en BRont
                    mouvementsTemp = ('B','Ui','Bi','U','Ri','U','R')
            elif c.cube_contient_couleur('FU',2,3): # cube bleu rouge en  FUx
                if c.get_facette('FU',1)==2: # bleu en haut
                    mouvementsTemp = ('U2','B','U','Bi','U','B','Ui','Bi')
                elif c.get_facette('FU',1)==3: # rouge en haut
                    mouvementsTemp = ('Ui','Ri','U2','R','Ui','Ri','U','R') # a faire
            elif c.cube_contient_couleur('RU',2,3):
                if c.get_facette('RU',1)==2: # bleu up
                    mouvementsTemp = ('B','U','Bi','U2','B','U','Bi','Ui','B','U','Bi')
                if c.get_facette('RU',1)==3:
                    mouvementsTemp = ('Ri','U2','R','U','Ri','Ui','R')
            elif c.cube_contient_couleur('BU',2,3):
                if c.get_facette('BU',1)==2:
                    mouvementsTemp = ('B','U2','Bi','Ui','B','U','Bi')
                if c.get_facette('BU',1)==3:
                    mouvementsTemp = ('Ri','Ui','R','U2','Ri','Ui','R','U','Ri','Ui','R')
            elif c.cube_contient_couleur('LU',2,3):
                if c.get_facette('LU',1)==2:
                    mouvementsTemp = ('U','B','U2','Bi','U','B','Ui','Bi')
                if c.get_facette('LU',1)==3:
                    mouvementsTemp = ('U2','Ri','Ui','R','Ui','Ri','U','R')
        elif c.get_facette('RBU',2)==2: # face bleu en haut
            if c.cube_contient_couleur('BR',2,3):
                if c.get_facette('BR',1)==2:
                    mouvementsTemp = ('Ui','B','Ui','Bi','Ui','B','U2','Bi')
                elif c.get_facette('BR',1)==3:
                    mouvementsTemp = ('Ui','B','U','Bi','U','Ri','Ui','R')
            elif c.cube_contient_couleur('FU',2,3):
                if c.get_facette('FU',1)==2:
                    mouvementsTemp = ('Ui','B','U2','Bi','Ui','B','U2','Bi')
                elif c.get_facette('FU',1)==3:
                    mouvementsTemp = ('Ri','Ui','R')
            elif c.cube_contient_couleur('RU',2,3):
                if c.get_facette('RU',1)==2:
                    mouvementsTemp =  ('Ri','U','R','U2','B','U','Bi')
                if c.get_facette('RU',1)==3:
                    mouvementsTemp = ('U','Ri','U','R','Ui','Ri','Ui','R')
            elif c.cube_contient_couleur('BU',2,3):
                if c.get_facette('BU',1)==2:
                    mouvementsTemp = ('U','B','Ui','Bi')
                if c.get_facette('BU',1)==3:
                    mouvementsTemp = ('Ui','B','U2','Bi','U','Ri','Ui','R')
            elif c.cube_contient_couleur('LU',2,3):
                if c.get_facette('LU',1)==2:
                    mouvementsTemp = ('Ui','B','U','Bi','Ui','B','U2','Bi')
                if c.get_facette('LU',1)==3:
                    mouvementsTemp = ('U','Ri','Ui','R','Ui','Ri','Ui','R')
        elif c.get_facette('RBU',2)==3: # rouge en haut
            if c.cube_contient_couleur('BR',2,3):
                if c.get_facette('BR',1)==2:
                    mouvementsTemp = ('U','Ri','U','R','U','Ri','U2','R')
                elif c.get_facette('BR',1)==3:
                    mouvementsTemp = ('U','Ri','Ui','R','Ui','B','U','Bi')
            elif c.cube_contient_couleur('FU',2,3):
                if c.get_facette('FU',1)==2:
                    mouvementsTemp = ('Ui','B','U','Bi','U','B','U','Bi')
                elif c.get_facette('FU',1)==3:
                    mouvementsTemp = ('U','Ri','Ui','R','U','Ri','U2','R')
            elif c.cube_contient_couleur('RU',2,3):
                if c.get_facette('RU',1)==2:
                    mouvementsTemp = ('U','Ri','U2','R','Ui','B','U','Bi')
                if c.get_facette('RU',1)==3:
                    mouvementsTemp = ('Ui','Ri','U','R')
            elif c.cube_contient_couleur('BU',2,3):
                if c.get_facette('BU',1)==2:
                    mouvementsTemp = ('Ui','B','Ui','Bi','U','B','U','Bi')
                if c.get_facette('BU',1)==3:
                    mouvementsTemp = ('B','Ui','Bi','U2','Ri','Ui','R')
            elif c.cube_contient_couleur('LU',2,3):
                if c.get_facette('LU',1)==2:
                    mouvementsTemp = ('B','U','Bi')
                if c.get_facette('LU',1)==3:
                    mouvementsTemp = ('U','Ri','U2','R','U','Ri','U2','R')

    elif c.cube_contient_couleur('RBD',0,2,3):
        if c.get_facette('RBD',0)==0: # face blanche en front
            if c.cube_contient_couleur('BR',2,3):
                if c.get_facette('BR',1)==2:
                    mouvementsTemp = ('B','Ui','Bi','Ui','B','U','Bi','Ui','B','U2','Bi')
                elif c.get_facette('BR',1)==3:
                    mouvementsTemp = ('B','Ui','Bi','U','Ri','Ui','R','Ui','Ri','Ui','R')
            elif c.cube_contient_couleur('FU',2,3):
                if c.get_facette('FU',1)==2:
                    mouvementsTemp = ('U2','B','Ui','Bi','U','B','Ui','Bi')
                elif c.get_facette('FU',1)==3:
                    mouvementsTemp = ('Ui','Ri','Ui','R','U','Ri','Ui','R')
            elif c.cube_contient_couleur('RU',2,3):
                if c.get_facette('RU',1)==2:
                    mouvementsTemp = ('Ui','B','Ui','Bi','U','B','Ui','Bi')
                if c.get_facette('RU',1)==3:
                    mouvementsTemp = ('Ri','Ui','R','U','Ri','Ui','R')
            elif c.cube_contient_couleur('BU',2,3):
                if c.get_facette('BU',1)==2:
                    mouvementsTemp = ('B','Ui','Bi','U','B','Ui','Bi')
                if c.get_facette('BU',1)==3:
                    mouvementsTemp = ('U','Ri','Ui','R','U','Ri','Ui','R')
            elif c.cube_contient_couleur('LU',2,3):
                if c.get_facette('LU',1)==2:
                    mouvementsTemp = ('U','B','Ui','Bi','U','B','Ui','Bi')
                if c.get_facette('LU',1)==3:
                    mouvementsTemp = ('U2','Ri','Ui','R','U','Ri','Ui','R')
        elif c.get_facette('RBD',0)==2: # face rouge en front
            if c.cube_contient_couleur('BR',2,3):
                if c.get_facette('BR',1)==2:
                    pass # déjà bien placé
                elif c.get_facette('BR',1)==3:
                    mouvementsTemp = ('B','Ui','Bi','U','Ri','U2','R','U','Ri','U2','R')
            elif c.cube_contient_couleur('FU',2,3):
                if c.get_facette('FU',1)==2:
                    mouvementsTemp = ('U','Ri','U','R','U','B','Ui','Bi')
                elif c.get_facette('FU',1)==3:
                    mouvementsTemp = ('B','Ui','Bi','Ui','Ri','U','R')
            elif c.cube_contient_couleur('RU',2,3):
                if c.get_facette('RU',1)==2:
                    mouvementsTemp = ('U2','Ri','U','R','U','B','Ui','Bi')
                if c.get_facette('RU',1)==3:
                    mouvementsTemp = ('U','B','Ui','Bi','Ui','Ri','U','R')
            elif c.cube_contient_couleur('BU',2,3):
                if c.get_facette('BU',1)==2:
                    mouvementsTemp = ('Ui','Ri','U','R','U','B','Ui','Bi')
                if c.get_facette('BU',1)==3:
                    mouvementsTemp = ('U2','B','Ui','Bi','Ui','Ri','U','R')
            elif c.cube_contient_couleur('LU',2,3):
                if c.get_facette('LU',1)==2:
                    mouvementsTemp = ('Ri','U','R','U','B','Ui','Bi')
                if c.get_facette('LU',1)==3:
                    mouvementsTemp = ('Ui','B','Ui','Bi','Ui','Ri','U','R')
        elif c.get_facette('RBD',0)==3: # vert en front
            if c.cube_contient_couleur('BR',2,3):
                if c.get_facette('BR',1)==2:
                    mouvementsTemp = ('B','Ui','Bi','U','B','U2','Bi','U','B','Ui','Bi')
                elif c.get_facette('BR',1)==3:
                    mouvementsTemp = ('B','U','Bi','Ui','B','Ui','Bi','U2','Ri','Ui','R')
            elif c.cube_contient_couleur('FU',2,3):
                if c.get_facette('FU',1)==2:
                    mouvementsTemp = ('U2','B','U','Bi','Ui','B','U','Bi')
                elif c.get_facette('FU',1)==3:
                    mouvementsTemp = ('Ui','Ri','U','R','Ui','Ri','U','R')
            elif c.cube_contient_couleur('RU',2,3):
                if c.get_facette('RU',1)==2:
                    mouvementsTemp = ('Ui','B','U','Bi','Ui','B','U','Bi')
                if c.get_facette('RU',1)==3:
                    mouvementsTemp = ('Ri','U','R','Ui','Ri','U','R')
            elif c.cube_contient_couleur('BU',2,3):
                if c.get_facette('BU',1)==2:
                    mouvementsTemp = ('B','U','Bi','Ui','B','U','Bi')
                if c.get_facette('BU',1)==3:
                    mouvementsTemp = ('U','Ri','U','R','Ui','Ri','U','R')
            elif c.cube_contient_couleur('LU',2,3):
                if c.get_facette('LU',1)==2:
                    mouvementsTemp = ('U','B','U','Bi','Ui','B','U','Bi')
                if c.get_facette('LU',1)==3:
                    mouvementsTemp = ('U2','Ri','U','R','Ui','Ri','U','R')

    if len(mouvementsTemp) > 0:
        c.mouvements(mouvementsTemp) #on effectue les mouvements
        mouvementsTotal += mouvementsTemp
        mouvementsTemp = ()

    # Insertion de la pair vert orange
    if c.cube_contient_couleur('FL',3,4):
        mouvementsTemp = ('Li','U','L')

    if len(mouvementsTemp) > 0:
        c.mouvements(mouvementsTemp) #on effectue les mouvements
        mouvementsTotal += mouvementsTemp
        mouvementsTemp = ()

    if c.cube_contient_couleur('LFU',0,3,4):
        mouvementsTemp = ('U',)
    elif c.cube_contient_couleur('RBU',0,3,4):
        mouvementsTemp = ('Ui',)
    elif c.cube_contient_couleur('FRU',0,3,4):
        mouvementsTemp = ('U2',)
    elif c.cube_contient_couleur('LFD',0,3,4): # cube en down : chaque cas
        # doit etre traité séparement en fonction de où est le cube vert orange
        if c.cube_contient_couleur('LU',3,4): # a gauche
            mouvementsTemp = ('Li','U2','L','Ui')
        elif c.cube_contient_couleur('RU',3,4): # a droite
            mouvementsTemp = ('Li','Ui','L','U2')
        elif c.cube_contient_couleur('BU',3,4): # cube derriere
            mouvementsTemp = ('Li','U2','L','Ui')
        elif c.cube_contient_couleur('FU',3,4): # devant
            mouvementsTemp = ('Li','Ui','L','U2')
        elif c.cube_contient_couleur('BL',3,4): # bien placé
            mouvementsTemp = ('Li','Ui','L','U2')

    if len(mouvementsTemp) > 0:
        c.mouvements(mouvementsTemp) #on effectue les mouvements
        mouvementsTotal += mouvementsTemp
        mouvementsTemp = ()

    if c.cube_contient_couleur('BLU',0,3,4): # cube bleu rouge blanc en BLU
        if c.get_facette('BLU',2)==0: # face blanche en haut
            if c.cube_contient_couleur('BL',3,4):
                if c.get_facette('BL',0)==3:
                    mouvementsTemp = ('L','U','Li','Ui','L','U','Li','Ui','L','U','Li')
                elif c.get_facette('BL',0)==4:
                    mouvementsTemp = ('L','Ui','Li','U','Bi','U','B')
            elif c.cube_contient_couleur('RU',3,4):
                if c.get_facette('RU',1)==3:
                    mouvementsTemp = ('U2','L','U','Li','U','L','Ui','Li')
                elif c.get_facette('RU',1)==4:
                    mouvementsTemp = ('Ui','Bi','U2','B','Ui','Bi','U','B')
            elif c.cube_contient_couleur('BU',3,4):
                if c.get_facette('BU',1)==3:
                    mouvementsTemp = ('L','U','Li','U2','L','U','Li','Ui','L','U','Li')
                if c.get_facette('BU',1)==4:
                    mouvementsTemp = ('Bi','U2','B','U','Bi','Ui','B')
            elif c.cube_contient_couleur('LU',3,4):
                if c.get_facette('LU',1)==3:
                    mouvementsTemp = ('L','U2','Li','Ui','L','U','Li')
                if c.get_facette('LU',1)==4:
                    mouvementsTemp = ('Bi','Ui','B','U2','Bi','Ui','B','U','Bi','Ui','B')
            elif c.cube_contient_couleur('FU',3,4):
                if c.get_facette('FU',1)==3:
                    mouvementsTemp = ('U','L','U2','Li','U','L','Ui','Li')
                if c.get_facette('FU',1)==4:
                    mouvementsTemp = ('U2','Bi','Ui','B','Ui','Bi','U','B')
        elif c.get_facette('BLU',2)==3: # face vert en haut
            if c.cube_contient_couleur('BL',3,4):
                if c.get_facette('BL',0)==3:
                    mouvementsTemp = ('Ui','L','Ui','Li','Ui','L','U2','Li')
                elif c.get_facette('BL',0)==4:
                    mouvementsTemp = ('Ui','L','U','Li','U','Bi','Ui','B')
            elif c.cube_contient_couleur('RU',3,4):
                if c.get_facette('RU',1)==3:
                    mouvementsTemp = ('Ui','L','U2','Li','Ui','L','U2','Li')
                elif c.get_facette('RU',1)==4:
                    mouvementsTemp = ('Bi','Ui','B')
            elif c.cube_contient_couleur('BU',3,4):
                if c.get_facette('BU',1)==3:
                    mouvementsTemp =  ('Bi','U','B','U2','L','U','Li')
                if c.get_facette('BU',1)==4:
                    mouvementsTemp = ('U','Bi','U','B','Ui','Bi','Ui','B')
            elif c.cube_contient_couleur('LU',3,4):
                if c.get_facette('LU',1)==3:
                    mouvementsTemp = ('U','L','Ui','Li')
                if c.get_facette('LU',1)==4:
                    mouvementsTemp = ('Ui','L','U2','Li','U','Bi','Ui','B')
            elif c.cube_contient_couleur('FU',3,4):
                if c.get_facette('FU',1)==3:
                    mouvementsTemp = ('Ui','L','U','Li','Ui','L','U2','Li')
                if c.get_facette('FU',1)==4:
                    mouvementsTemp = ('U','Bi','Ui','B','Ui','Bi','Ui','B')
        elif c.get_facette('BLU',2)==4: # orange en haut
            if c.cube_contient_couleur('BL',3,4):
                if c.get_facette('BL',0)==3:
                    mouvementsTemp = ('U','Bi','U','B','U','Bi','U2','B')
                elif c.get_facette('BL',0)==4:
                    mouvementsTemp = ('U','Bi','Ui','B','Ui','L','U','Li')
            elif c.cube_contient_couleur('RU',3,4):
                if c.get_facette('RU',1)==3:
                    mouvementsTemp = ('Ui','L','U','Li','U','L','U','Li')
                elif c.get_facette('RU',1)==4:
                    mouvementsTemp = ('U','Bi','Ui','B','U','Bi','U2','B')
            elif c.cube_contient_couleur('BU',3,4):
                if c.get_facette('BU',1)==3:
                    mouvementsTemp = ('U','Bi','U2','B','Ui','L','U','Li')
                if c.get_facette('BU',1)==4:
                    mouvementsTemp = ('Ui','Bi','U','B')
            elif c.cube_contient_couleur('LU',3,4):
                if c.get_facette('LU',1)==3:
                    mouvementsTemp = ('Ui','L','Ui','Li','U','L','U','Li')
                if c.get_facette('LU',1)==4:
                    mouvementsTemp = ('L','Ui','Li','U2','Bi','Ui','B')
            elif c.cube_contient_couleur('FU',3,4):
                if c.get_facette('FU',1)==3:
                    mouvementsTemp = ('L','U','Li')
                if c.get_facette('FU',1)==4:
                    mouvementsTemp = ('U','Bi','U2','B','U','Bi','U2','B')
    elif c.cube_contient_couleur('BLD',0,3,4):
        if c.get_facette('BLD',0)==0: # face blanche en front
            if c.cube_contient_couleur('BL',3,4):
                if c.get_facette('BL',0)==3:
                    mouvementsTemp = ('L','Ui','Li','Ui','L','U','Li','Ui','L','U2','Li')
                elif c.get_facette('BL',0)==4:
                    mouvementsTemp = ('L','Ui','Li','U','Bi','Ui','B','Ui','Bi','Ui','B')
            elif c.cube_contient_couleur('RU',3,4):
                if c.get_facette('RU',1)==3:
                    mouvementsTemp = ('U2','L','Ui','Li','U','L','Ui','Li')
                elif c.get_facette('RU',1)==4:
                    mouvementsTemp = ('Ui','Bi','Ui','B','U','Bi','Ui','B')
            elif c.cube_contient_couleur('BU',3,4):
                if c.get_facette('BU',1)==3:
                    mouvementsTemp = ('Ui','L','Ui','Li','U','L','Ui','Li')
                if c.get_facette('BU',1)==4:
                    mouvementsTemp = ('Bi','Ui','B','U','Bi','Ui','B')
            elif c.cube_contient_couleur('LU',3,4):
                if c.get_facette('LU',1)==3:
                    mouvementsTemp = ('L','Ui','Li','U','L','Ui','Li')
                if c.get_facette('LU',1)==4:
                    mouvementsTemp = ('U','Bi','Ui','B','U','Bi','Ui','B')
            elif c.cube_contient_couleur('FU',3,4):
                if c.get_facette('FU',1)==3:
                    mouvementsTemp = ('U','L','Ui','Li','U','L','Ui','Li')
                if c.get_facette('FU',1)==4:
                    mouvementsTemp = ('U2','Bi','Ui','B','U','Bi','Ui','B')
        elif c.get_facette('BLD',0)==3: # face vert en front
            if c.cube_contient_couleur('BL',3,4):
                if c.get_facette('BL',0)==3:
                    pass # déjà bien placé
                elif c.get_facette('BL',0)==4:
                    mouvementsTemp = ('L','Ui','Li','U','Bi','U2','B','U','Bi','U2','B')
            elif c.cube_contient_couleur('RU',3,4):
                if c.get_facette('RU',1)==3:
                    mouvementsTemp = ('U','Bi','U','B','U','L','Ui','Li')
                elif c.get_facette('RU',1)==4:
                    mouvementsTemp = ('L','Ui','Li','Ui','Bi','U','B')
            elif c.cube_contient_couleur('BU',3,4):
                if c.get_facette('BU',1)==3:
                    mouvementsTemp = ('U2','Bi','U','B','U','L','Ui','Li')
                if c.get_facette('BU',1)==4:
                    mouvementsTemp = ('U','L','Ui','Li','Ui','Bi','U','B')
            elif c.cube_contient_couleur('LU',3,4):
                if c.get_facette('LU',1)==3:
                    mouvementsTemp = ('Ui','Bi','U','B','U','L','Ui','Li')
                if c.get_facette('LU',1)==4:
                    mouvementsTemp = ('U2','L','Ui','Li','Ui','Bi','U','B')
            elif c.cube_contient_couleur('FU',3,4):
                if c.get_facette('FU',1)==3:
                    mouvementsTemp = ('Bi','U','B','U','L','Ui','Li')
                if c.get_facette('FU',1)==4:
                    mouvementsTemp = ('Ui','L','Ui','Li','Ui','Bi','U','B')
        elif c.get_facette('BLD',0)==4: # orange en front
            if c.cube_contient_couleur('BL',3,4):
                if c.get_facette('BL',0)==3:
                    mouvementsTemp = ('L','Ui','Li','U','L','U2','Li','U','L','Ui','Li')
                elif c.get_facette('BL',0)==4:
                    mouvementsTemp = ('L','U','Li','Ui','L','Ui','Li','U2','Bi','Ui','B')
            elif c.cube_contient_couleur('RU',3,4):
                if c.get_facette('RU',1)==3:
                    mouvementsTemp = ('U2','L','U','Li','Ui','L','U','Li')
                elif c.get_facette('RU',1)==4:
                    mouvementsTemp = ('Ui','Bi','U','B','Ui','Bi','U','B')
            elif c.cube_contient_couleur('BU',3,4):
                if c.get_facette('BU',1)==3:
                    mouvementsTemp = ('Ui','L','U','Li','Ui','L','U','Li')
                if c.get_facette('BU',1)==4:
                    mouvementsTemp = ('Bi','U','B','Ui','Bi','U','B')
            elif c.cube_contient_couleur('LU',3,4):
                if c.get_facette('LU',1)==3:
                    mouvementsTemp = ('L','U','Li','Ui','L','U','Li')
                if c.get_facette('LU',1)==4:
                    mouvementsTemp = ('U','Bi','U','B','Ui','Bi','U','B')
            elif c.cube_contient_couleur('FU',3,4):
                if c.get_facette('FU',1)==3:
                    mouvementsTemp = ('U','L','U','Li','Ui','L','U','Li')
                if c.get_facette('FU',1)==4:
                    mouvementsTemp = ('U2','Bi','U','B','Ui','Bi','U','B')

    if len(mouvementsTemp) > 0:
        c.mouvements(mouvementsTemp) #on effectue les mouvements
        mouvementsTotal += mouvementsTemp
        mouvementsTemp = ()

    # Insertion bleu orange
    # Le cube Orange bleu blanc doit etre en LFU ou LFD
    if c.cube_contient_couleur('FRU',0,1,4):
        mouvementsTemp = ('U',)
    elif c.cube_contient_couleur('BLU',0,1,4):
        mouvementsTemp = ('Ui',)
    elif c.cube_contient_couleur('RBU',0,1,4):
        mouvementsTemp = ('U2',)

    if len(mouvementsTemp) > 0:
        c.mouvements(mouvementsTemp) #on effectue les movements
        mouvementsTotal += mouvementsTemp
        mouvementsTemp = ()

    if c.cube_contient_couleur('LFU',0,1,4): # cube orange bleu blanc en LFU
        if c.get_facette('LFU',2)==0: # face blanche en haut
            if c.cube_contient_couleur('FL',1,4):
                if c.get_facette('FL',1)==4:
                    mouvementsTemp = ('F','U','Fi','Ui','F','U','Fi','Ui','F','U','Fi')
                elif c.get_facette('FL',1)==1:
                    mouvementsTemp = ('F','Ui','Fi','U','Li','U','L')
            elif c.cube_contient_couleur('BU',1,4):
                if c.get_facette('BU',1)==4:
                    mouvementsTemp = ('U2','F','U','Fi','U','F','Ui','Fi')
                elif c.get_facette('BU',1)==1:
                    mouvementsTemp = ('Ui','Li','U2','L','Ui','Li','U','L')
            elif c.cube_contient_couleur('LU',1,4):
                if c.get_facette('LU',1)==4:
                    mouvementsTemp = ('F','U','Fi','U2','F','U','Fi','Ui','F','U','Fi')
                if c.get_facette('LU',1)==1:
                    mouvementsTemp = ('Li','U2','L','U','Li','Ui','L')
            elif c.cube_contient_couleur('FU',1,4):
                if c.get_facette('FU',1)==4:
                    mouvementsTemp = ('F','U2','Fi','Ui','F','U','Fi')
                if c.get_facette('FU',1)==1:
                    mouvementsTemp = ('Li','Ui','L','U2','Li','Ui','L','U','Li','Ui','L')
            elif c.cube_contient_couleur('RU',1,4):
                if c.get_facette('RU',1)==4:
                    mouvementsTemp = ('U','F','U2','Fi','U','F','Ui','Fi')
                if c.get_facette('RU',1)==1:
                    mouvementsTemp = ('U2','Li','Ui','L','Ui','Li','U','L')
        elif c.get_facette('LFU',2)==4: # face orange en haut
            if c.cube_contient_couleur('FL',1,4):
                if c.get_facette('FL',1)==4:
                    mouvementsTemp = ('Ui','F','Ui','Fi','Ui','F','U2','Fi')
                elif c.get_facette('FL',1)==1:
                    mouvementsTemp = ('Ui','F','U','Fi','U','Li','Ui','L')
            elif c.cube_contient_couleur('BU',1,4):
                if c.get_facette('BU',1)==4:
                    mouvementsTemp = ('Ui','F','U2','Fi','Ui','F','U2','Fi')
                elif c.get_facette('BU',1)==1:
                    mouvementsTemp = ('Li','Ui','L')
            elif c.cube_contient_couleur('LU',1,4):
                if c.get_facette('LU',1)==4:
                    mouvementsTemp =  ('Li','U','L','U2','F','U','Fi')
                if c.get_facette('LU',1)==1:
                    mouvementsTemp = ('U','Li','U','L','Ui','Li','Ui','L')
            elif c.cube_contient_couleur('FU',1,4):
                if c.get_facette('FU',1)==4:
                    mouvementsTemp = ('U','F','Ui','Fi')
                if c.get_facette('FU',1)==1:
                    mouvementsTemp = ('Ui','F','U2','Fi','U','Li','Ui','L')
            elif c.cube_contient_couleur('RU',1,4):
                if c.get_facette('RU',1)==4:
                    mouvementsTemp = ('Ui','F','U','Fi','Ui','F','U2','Fi')
                if c.get_facette('RU',1)==1:
                    mouvementsTemp = ('U','Li','Ui','L','Ui','Li','Ui','L')
        elif c.get_facette('LFU',2)==1: # bleu en haut
            if c.cube_contient_couleur('FL',1,4):
                if c.get_facette('FL',1)==4:
                    mouvementsTemp = ('U','Li','U','L','U','Li','U2','L')
                elif c.get_facette('FL',1)==1:
                    mouvementsTemp = ('U','Li','Ui','L','Ui','F','U','Fi')
            elif c.cube_contient_couleur('BU',1,4):
                if c.get_facette('BU',1)==4:
                    mouvementsTemp = ('Ui','F','U','Fi','U','F','U','Fi')
                elif c.get_facette('BU',1)==1:
                    mouvementsTemp = ('U','Li','Ui','L','U','Li','U2','L')
            elif c.cube_contient_couleur('LU',1,4):
                if c.get_facette('LU',1)==4:
                    mouvementsTemp = ('U','Li','U2','L','Ui','F','U','Fi')
                if c.get_facette('LU',1)==1:
                    mouvementsTemp = ('Ui','Li','U','L')
            elif c.cube_contient_couleur('FU',1,4):
                if c.get_facette('FU',1)==4:
                    mouvementsTemp = ('Ui','F','Ui','Fi','U','F','U','Fi')
                if c.get_facette('FU',1)==1:
                    mouvementsTemp = ('F','Ui','Fi','U2','Li','Ui','L')
            elif c.cube_contient_couleur('RU',1,4):
                if c.get_facette('RU',1)==4:
                    mouvementsTemp = ('F','U','Fi')
                if c.get_facette('RU',1)==1:
                    mouvementsTemp = ('U','Li','U2','L','U','Li','U2','L')
    elif c.cube_contient_couleur('LFD',0,1,4):
        if c.get_facette('LFD',0)==0: # face blanche en front
            if c.cube_contient_couleur('FL',1,4):
                if c.get_facette('FL',1)==4:
                    mouvementsTemp = ('F','Ui','Fi','Ui','F','U','Fi','Ui','F','U2','Fi')
                elif c.get_facette('FL',1)==1:
                    mouvementsTemp = ('F','Ui','Fi','U','Li','Ui','L','Ui','Li','Ui','L')
            elif c.cube_contient_couleur('BU',1,4):
                if c.get_facette('BU',1)==4:
                    mouvementsTemp = ('U2','F','Ui','Fi','U','F','Ui','Fi')
                elif c.get_facette('BU',1)==1:
                    mouvementsTemp = ('Ui','Li','Ui','L','U','Li','Ui','L')
            elif c.cube_contient_couleur('LU',1,4):
                if c.get_facette('LU',1)==4:
                    mouvementsTemp = ('Ui','F','Ui','Fi','U','F','Ui','Fi')
                if c.get_facette('LU',1)==1:
                    mouvementsTemp = ('Li','Ui','L','U','Li','Ui','L')
            elif c.cube_contient_couleur('FU',1,4):
                if c.get_facette('FU',1)==4:
                    mouvementsTemp = ('F','Ui','Fi','U','F','Ui','Fi')
                if c.get_facette('FU',1)==1:
                    mouvementsTemp = ('U','Li','Ui','L','U','Li','Ui','L')
            elif c.cube_contient_couleur('RU',1,4):
                if c.get_facette('RU',1)==4:
                    mouvementsTemp = ('U','F','Ui','Fi','U','F','Ui','Fi')
                if c.get_facette('RU',1)==1:
                    mouvementsTemp = ('U2','Li','Ui','L','U','Li','Ui','L')
        elif c.get_facette('LFD',0)==4: # face orange en front
            if c.cube_contient_couleur('FL',1,4):
                if c.get_facette('FL',1)==4:
                    pass # déjà bien placé
                elif c.get_facette('FL',1)==1:
                    mouvementsTemp = ('F','Ui','Fi','U','Li','U2','L','U','Li','U2','L')
            elif c.cube_contient_couleur('BU',1,4):
                if c.get_facette('BU',1)==4:
                    mouvementsTemp = ('U','Li','U','L','U','F','Ui','Fi')
                elif c.get_facette('BU',1)==1:
                    mouvementsTemp = ('F','Ui','Fi','Ui','Li','U','L')
            elif c.cube_contient_couleur('LU',1,4):
                if c.get_facette('LU',1)==4:
                    mouvementsTemp = ('U2','Li','U','L','U','F','Ui','Fi')
                if c.get_facette('LU',1)==1:
                    mouvementsTemp = ('U','F','Ui','Fi','Ui','Li','U','L')
            elif c.cube_contient_couleur('FU',1,4):
                if c.get_facette('FU',1)==4:
                    mouvementsTemp = ('Ui','Li','U','L','U','F','Ui','Fi')
                if c.get_facette('FU',1)==1:
                    mouvementsTemp = ('U2','F','Ui','Fi','Ui','Li','U','L')
            elif c.cube_contient_couleur('RU',1,4):
                if c.get_facette('RU',1)==4:
                    mouvementsTemp = ('Li','U','L','U','F','Ui','Fi')
                if c.get_facette('RU',1)==1:
                    mouvementsTemp = ('Ui','F','Ui','Fi','Ui','Li','U','L')
        elif c.get_facette('LFD',0)==1: # bleu en front
            if c.cube_contient_couleur('FL',1,4):
                if c.get_facette('FL',1)==4:
                    mouvementsTemp = ('F','Ui','Fi','U','F','U2','Fi','U','F','Ui','Fi')
                elif c.get_facette('FL',1)==1:
                    mouvementsTemp = ('F','U','Fi','Ui','F','Ui','Fi','U2','Li','Ui','L')
            elif c.cube_contient_couleur('BU',1,4):
                if c.get_facette('BU',1)==4:
                    mouvementsTemp = ('U2','F','U','Fi','Ui','F','U','Fi')
                elif c.get_facette('BU',1)==1:
                    mouvementsTemp = ('Ui','Li','U','L','Ui','Li','U','L')
            elif c.cube_contient_couleur('LU',1,4):
                if c.get_facette('LU',1)==4:
                    mouvementsTemp = ('Ui','F','U','Fi','Ui','F','U','Fi')
                if c.get_facette('LU',1)==1:
                    mouvementsTemp = ('Li','U','L','Ui','Li','U','L')
            elif c.cube_contient_couleur('FU',1,4):
                if c.get_facette('FU',1)==4:
                    mouvementsTemp = ('F','U','Fi','Ui','F','U','Fi')
                if c.get_facette('FU',1)==1:
                    mouvementsTemp = ('U','Li','U','L','Ui','Li','U','L')
            elif c.cube_contient_couleur('RU',1,4):
                if c.get_facette('RU',1)==4:
                    mouvementsTemp = ('U','F','U','Fi','Ui','F','U','Fi')
                if c.get_facette('RU',1)==1:
                    mouvementsTemp = ('U2','Li','U','L','Ui','Li','U','L')

    if len(mouvementsTemp) > 0:
        c.mouvements(mouvementsTemp) #on effectue les movements
        mouvementsTotal += mouvementsTemp
        mouvementsTemp = ()

    return c,mouvementsTotal

def oll(c):
    '''
        Etape 3 de l'algo CFOP
        Faire la face jaune, exemple :
               W W W
               W W W
               W W W
        O O O  G G G  R R R  B B B
        O O O  G G G  R R R  B B B
        X X X  X X X  X X X  X X X
               Y Y Y
               Y Y Y
               Y Y Y

        :Args:
            c {Cube}, mouvements {String} l'objet cube, à résoudre
    def Cross(c):

        :Returns:
            {Cube}, {String} L'objet cube avec la face jaune de faite
                             Liste des mouvements à faire
    '''
    mouvementsTemp = ()
    mouvementsTotal = ()

    # Test si on à pas déjà la croix
    if c.get_facette('FU',1)!=5 or c.get_facette('RU',1)!=5 \
        or c.get_facette('BU',1)!=5 or c.get_facette('LU',1)!=5:

        # Test de tout les cas possible
        if c.get_facette('FU',1)!=5 and c.get_facette('RU',1)!=5 \
            and c.get_facette('BU',1)!=5 and c.get_facette('LU',1)!=5:
            # Test si aucune des disposition, on fait une suite de rotation pour avoir un petit L ou une ligne
            mouvementsTemp = ('F','U','R','Ui','Ri','Fi')
            c.mouvements(mouvementsTemp) # On effectue la liste de mouvements de la partie 1 (qui est optionnelle)
            mouvementsTotal += mouvementsTemp
            mouvementsTemp = ()

        #Cas ou on a une forme jaune en L sur la face du haut (U)

        # Test disposition en L n°1
        if c.get_facette('LU',1)==5 and c.get_facette('BU',1)==5 \
            and c.get_facette('FU',1)!=5 and c.get_facette('RU',1)!=5:
            mouvementsTemp = ('F','U','R','Ui','Ri','Fi')
        # Test disposition en L n°2
        elif c.get_facette('BU',1)==5 and c.get_facette('RU',1)==5 \
            and c.get_facette('LU',1)!=5 and c.get_facette('FU',1)!=5:
            mouvementsTemp = ('L','U','F','Ui','Fi','Li')
        # Test disposition en L n°3
        elif c.get_facette('RU',1)==5 and c.get_facette('FU',1)==5 \
            and c.get_facette('LU',1)!=5 and c.get_facette('BU',1)!=5:
            mouvementsTemp = ('B','U','L','Ui','Li','Bi')
        # Test disposition en L n°4
        elif c.get_facette('FU',1)==5 and c.get_facette('LU',1)==5 \
            and c.get_facette('BU',1)!=5 and c.get_facette('RU',1)!=5:
            mouvementsTemp = ('R','U','B','Ui','Bi','Ri')

        # Cas ou on à une ligne jaune sur la face du haut (U)

        # Test ligne n°1
        elif (c.get_facette('LU',1)==5 and c.get_facette('RU',1)==5 \
            and c.get_facette('BU',1)!=5 and c.get_facette('FU',1)!=5):
            mouvementsTemp = ('F','R','U','Ri','Ui','Fi')
        # Test ligne n°2
        elif c.get_facette('BU',1)==5 and c.get_facette('FU',1)==5 \
            and c.get_facette('RU',1)!=5 and c.get_facette('LU',1)!=5:
            mouvementsTemp = ('R','B','U','Bi','Ui','Ri')

        #On effectue la liste de mouvement de la partie 2
        c.mouvements(mouvementsTemp)
        mouvementsTotal += mouvementsTemp
        mouvementsTemp = ()

    #Test de la croix jaune
    if c.get_facette('FU',1)==5 and c.get_facette('RU',1)==5 \
        and c.get_facette('BU',1)==5 and c.get_facette('LU',1)==5:

        #Cas numéro 1
        if (c.get_facette('FRU',0)==5 and c.get_facette('LFU',1)==5 \
            and c.get_facette('BLU',0)==5 and c.get_facette("RBU",1)):
            mouvementsTemp = ('R','U2','Ri','Ui','R','U','Ri','Ui','R','Ui','Ri')
        #cas numéro 1 : autre configration dans l'espace
        elif (c.get_facette('LFU',0)==5 and c.get_facette('BLU',1)==5\
            and c.get_facette('FRU',1)==5 and c.get_facette('RBU',0)==5):
            mouvementsTemp = ('B','U2','Bi','Ui','B','U','Bi','Ui','B','Ui','Bi')

        #cas numéro 2
        elif (c.get_facette('FRU',0)==5 and c.get_facette('LFU',0)==5\
            and c.get_facette('BLU',1)==5 and c.get_facette('RBU',1)==5):
            mouvementsTemp = ('R','U2','R2','Ui','R2','Ui','R2','U2','R')
        #Cas numéro 2 : autre configuration dans l'espace
        elif (c.get_facette('FRU',0)==5 and c.get_facette('LFU',1)==5\
            and c.get_facette('BLU',1)==5 and c.get_facette('RBU',0)==5):
            mouvementsTemp = ('B','U2','B2','Ui','B2','Ui','B2','U2','B')
        #Cas numéro 2 : autre configuration dans l'espace
        elif (c.get_facette('FRU',1)==5 and c.get_facette('LFU',1)==5\
            and c.get_facette('BLU',0)==5 and c.get_facette('RBU',0)==5):
            mouvementsTemp = ('L','U2','L2','Ui','L2','Ui','L2','U2','L')
        #Cas numéro 2 : autre configuration dans l'espace
        elif (c.get_facette('FRU',1)==5 and c.get_facette('LFU',0)==5\
            and c.get_facette('BLU',0)==5 and c.get_facette('RBU',1)==5):
            mouvementsTemp = ('F','U2','F2','Ui','F2','Ui','F2','U2','F')

        #Cas numéro 3
        elif (c.get_facette('LFU',2)==5 and c.get_facette('FRU',0)==5\
            and c.get_facette('FRU',2)!=5 and c.get_facette('BLU',2)!=5 \
            and c.get_facette('RBU',2)!=5):
            mouvementsTemp = ('R','U','Ri','U','R','U2','Ri')
        #Cas numéro 3 / autre disposition
        elif (c.get_facette('FRU',2)==5 and c.get_facette('RBU',0)==5\
            and c.get_facette('LFU',2)!=5 and c.get_facette('BLU',2)!=5 \
            and c.get_facette('RBU',2)!=5):
            mouvementsTemp = ('B','U','Bi','U','B','U2','Bi')
        #Cas numéro 3 / autre disposition
        elif (c.get_facette('RBU',2)==5 and c.get_facette('BLU',0)==5\
            and c.get_facette('FRU',2)!=5 and c.get_facette('LFU',2)!=5 \
            and c.get_facette('RBU',0)!=5):
            mouvementsTemp = ('L','U','Li','U','L','U2','Li')
        #Cas numéro 3 / autre disposition
        elif (c.get_facette('BLU',2)==5 and c.get_facette('LFU',0)==5\
            and c.get_facette('FRU',2)!=5 and c.get_facette('LFU',2)!=5 \
            and c.get_facette('RBU',2)!=5):
            mouvementsTemp = ('F','U','Fi','U','F','U2','Fi')

        #Cas numéro 4
        elif (c.get_facette('RBU',2)==5 and c.get_facette('BLU',2)!=5\
            and c.get_facette('FRU',2)!=5 and c.get_facette('LFU',2)!=5\
            and c.get_facette('BLU',0)!=5):
            mouvementsTemp = ('R','U2','Ri','Ui','R','Ui','Ri')
        #Cas numéro 4 / autre disposition
        elif (c.get_facette('BLU',2)==5 and c.get_facette('LFU',2)!=5\
            and c.get_facette('FRU',2)!=5 and c.get_facette('RBU',2)!=5\
            and c.get_facette('LFU',0)!=5):
            mouvementsTemp = ('B','U2','Bi','Ui','B','Ui','Bi')
        #Cas numéro 4 / autre disposition
        elif (c.get_facette('LFU',2)==5 and c.get_facette('FRU',2)!=5\
            and c.get_facette('RBU',2)!=5 and c.get_facette('BLU',2)!=5\
            and c.get_facette('FRU',0)!=5):
            mouvementsTemp = ('L','U2','Li','Ui','L','Ui','Li')
        #Cas numéro 4 / autre disposition
        elif (c.get_facette('FRU',2)==5 and c.get_facette('RBU',2)!=5\
            and c.get_facette('LFU',2)!=5 and c.get_facette('BLU',2)!=5\
            and c.get_facette('RBU',0)!=5):
            mouvementsTemp = ('F','U2','Fi','Ui','F','Ui','Fi')

        #Cas numéro 5
        elif (c.get_facette('FRU',0)==5 and c.get_facette('LFU',1)==5\
            and c.get_facette('BLU',2)==5 and c.get_facette('RBU',2)==5):
            mouvementsTemp = ('R2','D','Ri','U2','R','Di','Ri','U2','Ri')
        #Cas numéro 5 / autre disposition
        elif (c.get_facette('FRU',1)==5 and c.get_facette('LFU',2)==5\
            and c.get_facette('BLU',2)==5 and c.get_facette('RBU',0)==5):
            mouvementsTemp = ('B2','D','Bi','U2','B','Di','Bi','U2','Bi')
        #Cas numéro 5 / autre disposition
        elif (c.get_facette('FRU',2)==5 and c.get_facette('LFU',2)==5\
            and c.get_facette('BLU',0)==5 and c.get_facette('RBU',1)==5):
            mouvementsTemp = ('L2','D','Li','U2','L','Di','Li','U2','Li')
        #Cas numéro 5 / autre disposition
        elif (c.get_facette('FRU',2)==5 and c.get_facette('LFU',0)==5\
            and c.get_facette('BLU',1)==5 and c.get_facette('RBU',2)==5):
            mouvementsTemp = ('F2','D','Fi','U2','F','Di','Fi','U2','Fi')

        #Cas numéro 6
        elif (c.get_facette('FRU',2)==5 and c.get_facette('LFU',1)==5\
            and c.get_facette('BLU',0)==5 and c.get_facette('RBU',2)==5):
            mouvementsTemp = ('L','F','Ri','Fi','Li','F','R','Fi')
        #Cas numéro 6 / autre disposition
        elif (c.get_facette('FRU',1)==5 and c.get_facette('LFU',0)==5\
            and c.get_facette('BLU',2)==5 and c.get_facette('RBU',2)==5):
            mouvementsTemp = ('F','R','Bi','Ri','Fi','R','B','Ri')
        #Cas numéro 6 / autre disposition
        elif (c.get_facette('FRU',0)==5 and c.get_facette('LFU',2)==5\
            and c.get_facette('BLU',2)==5 and c.get_facette('RBU',1)==5):
            mouvementsTemp = ('R','B','Li','Bi','Ri','B','L','Bi')
        #Cas numéro 6 / autre disposition
        elif (c.get_facette('FRU',2)==5 and c.get_facette('LFU',2)==5\
            and c.get_facette('BLU',1)==5 and c.get_facette('RBU',0)==5):
            mouvementsTemp = ('B','L','Fi','Li','Bi','L','F','Li')

        #Cas numéro 7
        elif (c.get_facette('FRU',0)==5 and c.get_facette('LFU',2)==5\
            and c.get_facette('RBU',2)==5 and c.get_facette('BLU',1)==5):
            mouvementsTemp = ('Fi','L','F','Ri','Fi','Li','F','R')
        #Cas numéro 7 / autre disposition
        elif (c.get_facette('FRU',2)==5 and c.get_facette('LFU',1)==5\
            and c.get_facette('BLU',2)==5 and c.get_facette('RBU',0)==5):
            mouvementsTemp = ('Ri','F','R','Bi','Ri','Fi','R','B')
        #Cas numéro 7 / autre disposition
        elif (c.get_facette('FRU',1)==5 and c.get_facette('LFU',2)==5\
            and c.get_facette('BLU',0)==5 and c.get_facette('RBU',2)==5):
            mouvementsTemp = ('Bi','R','B','Li','Bi','Ri','B','L')
        #Cas numéro 7 / autre disposition
        elif (c.get_facette('FRU',2)==5 and c.get_facette('LFU',0)==5\
            and c.get_facette('BLU',2)==5 and c.get_facette('RBU',1)==5):
            mouvementsTemp = ('Li','B','L','Fi','Li','Bi','L','F')
        c.mouvements(mouvementsTemp)
        mouvementsTotal += mouvementsTemp
        mouvementsTemp = ()

    return c, mouvementsTotal

def pll(c):
    '''
    pll

    Etape 4 et dernière étape de l'algo CFOP
    Finir le rubik's cube, exemple :
               W W W
               W W W
               W W W
    O O O  G G G  R R R  B B B
    O O O  G G G  R R R  B B B
    O O O  G G G  R R R  B B B
               Y Y Y
               Y Y Y
               Y Y Y

    :Args:
        c           {Cube}      l'objet cube
        mouvements  {String}

    :Returns:
        {Cube}          L'objet cube avec la face jaune de faite,
        {String|None}   Liste des mouvements à faire, ou rien si cube pas resolvable
    '''

    mouvementsTemp = ()    #liste des mouvements à effectués durant l'algo
    mouvementsTotal = () # liste des mouvements qui vont etre renvoyé

    #On place correctement les coins du haut
    if ((c.cube_contient_couleur('BLU',3,4,5) and c.cube_contient_couleur('RBU',2,3,5)) #si on a 2 coins déjà bien placés
        or (c.cube_contient_couleur('RBU',2,3,5) and c.cube_contient_couleur('FRU',1,2,5))
        or (c.cube_contient_couleur('FRU',1,2,5) and c.cube_contient_couleur('LFU',4,1,5))
        or (c.cube_contient_couleur('LFU',4,1,5) and c.cube_contient_couleur('BLU',3,4,5))
        or (c.cube_contient_couleur('BLU',3,4,5) and c.cube_contient_couleur('FRU',1,2,5))
        or (c.cube_contient_couleur('RBU',2,3,5) and c.cube_contient_couleur('LFU',4,1,5))):
        pass # alors ya rien à faire
    elif (c.cube_contient_couleur('BLU',4,1,5) and (c.cube_contient_couleur('RBU',3,4,5))) or \
        (c.cube_contient_couleur('RBU',3,4,5) and (c.cube_contient_couleur('FRU',2,3,5))) or \
        (c.cube_contient_couleur('FRU',2,3,5) and (c.cube_contient_couleur('LFU',1,2,5))) or \
        (c.cube_contient_couleur('LFU',1,2,5) and (c.cube_contient_couleur('BLU',4,1,5))) or \
        (c.cube_contient_couleur('BLU',4,1,5) and (c.cube_contient_couleur('FRU',2,3,5))) or \
        (c.cube_contient_couleur('LFU',1,2,5) and (c.cube_contient_couleur('RBU',3,4,5))):
        mouvementsTemp = ('Ui',) #cas ou ya qu'un mouvement Ui à faire pour obtenir 2 coins bien placés
    elif (c.cube_contient_couleur('BLU',2,3,5) and (c.cube_contient_couleur('RBU',1,2,5))) or \
        (c.cube_contient_couleur('RBU',1,2,5) and (c.cube_contient_couleur('FRU',4,1,5))) or \
        (c.cube_contient_couleur('FRU',4,1,5) and (c.cube_contient_couleur('LFU',3,4,5))) or \
        (c.cube_contient_couleur('LFU',3,4,5) and (c.cube_contient_couleur('BLU',2,3,5))) or \
        (c.cube_contient_couleur('BLU',2,3,5) and (c.cube_contient_couleur('FRU',4,1,5))) or \
        (c.cube_contient_couleur('LFU',3,4,5) and (c.cube_contient_couleur('RBU',1,2,5))):
        mouvementsTemp = ('U',) #cas ou ya qu'un mouvement U à faire pour obtenir 2 coins bien placés
    else:
        mouvementsTemp = ('U2',) # si on a pas un cas précédent alors il faut faire 2 U

    if len(mouvementsTemp) > 0:
        c.mouvements(mouvementsTemp) #on effectue les mouvements
        mouvementsTotal += mouvementsTemp
        mouvementsTemp = ()

    if c.cube_contient_couleur('BLU',3,4,5) \
        and c.cube_contient_couleur('RBU',2,3,5) \
        and c.cube_contient_couleur('FRU',1,2,5) \
        and c.cube_contient_couleur('LFU',4,1,5):
            pass #les 4 Coins sont déjà bien placés
    #Coins bien placés au fond
    elif c.cube_contient_couleur('BLU',3,4,5) and c.cube_contient_couleur('RBU',2,3,5):
        mouvementsTemp = ('Ri','F','Ri','B','B','R','Fi','Ri','B','B','R','R','Ui')
    #Coins biens placés à droite
    elif c.cube_contient_couleur('RBU',2,3,5) and c.cube_contient_couleur('FRU',1,2,5):
        mouvementsTemp = ('Fi','L','Fi','R','R','F','Li','Fi','R','R','F','F','Ui')
    #Coins bien placés devant
    elif c.cube_contient_couleur('FRU',1,2,5) and c.cube_contient_couleur('LFU',4,1,5):
        mouvementsTemp = ('Li','B','Li','F','F','L','Bi','Li','F','F','L','L','Ui')
    #Coins bien placés à gauche
    elif c.cube_contient_couleur('LFU',4,1,5) and c.cube_contient_couleur('BLU',3,4,5):
        mouvementsTemp = ('Bi','R','Bi','L','L','B','Ri','Bi','L','L','B','B','Ui')
    #coins bien placés en diagonale #1
    elif c.cube_contient_couleur('BLU',3,4,5) and c.cube_contient_couleur('FRU',1,2,5):
        mouvementsTemp = ('Ri','F','Ri','B','B','R','Fi','Ri','B','B','R','R','Ui')
        c.mouvements(mouvementsTemp)
        mouvementsTotal += mouvementsTemp
        mouvementsTemp = ()
        c, mouvementsTemp = pll(c) #on a besoin de rappeller pll dessus
        mouvementsTotal += mouvementsTemp
        return c, mouvementsTotal
    #coins bien placés en diagonale #2
    elif c.cube_contient_couleur('RBU',2,3,5) and c.cube_contient_couleur('LFU',4,1,5):
        mouvementsTemp = ('Ri','F','Ri','B','B','R','Fi','Ri','B','B','R','R','Ui')
        c.mouvements(mouvementsTemp)
        mouvementsTotal += mouvementsTemp
        mouvementsTemp = ()
        c, mouvementsTemp = pll(c) #on a besoin de rappeller pll dessus
        mouvementsTotal += mouvementsTemp
        return c, mouvementsTotal

    if len(mouvementsTemp) > 0:
        c.mouvements(mouvementsTemp) #on effectue les mouvements
        mouvementsTotal += mouvementsTemp
        mouvementsTemp = ()

    #on positionne maintenant les arêtes jaunes

    if c.cube_contient_couleur('LU',4,5):# si c'est le coin gauche qui est bien placé
        if c.cube_contient_couleur('FU',3,5) :
            mouvementsTemp = ('R','R','U','F','Bi','R','R','Fi','B','U','R','R')
            c.mouvements(mouvementsTemp) #on effectue les mouvements
            mouvementsTotal += mouvementsTemp
            mouvementsTemp = ()
        elif c.cube_contient_couleur('FU',2,5):
            mouvementsTemp = ('R','R','Ui','F','Bi','R','R','Fi','B','Ui','R','R')
            c.mouvements(mouvementsTemp) #on effectue les mouvements
            mouvementsTotal += mouvementsTemp
            mouvementsTemp = ()

    elif c.cube_contient_couleur('BU',3,5): # coin B bien placé
        if c.cube_contient_couleur('FU',2,5):
            mouvementsTemp = ('F','F','Ui','L','Ri','F','F','Li','R','Ui','F','F')
            c.mouvements(mouvementsTemp) #on effectue les mouvements
            mouvementsTotal += mouvementsTemp
            mouvementsTemp = ()
        elif c.cube_contient_couleur('FU',4,5):
            mouvementsTemp = ('F','F','U','L','Ri','F','F','Li','R','U','F','F')
            c.mouvements(mouvementsTemp) #on effectue les mouvements
            mouvementsTotal += mouvementsTemp
            mouvementsTemp = ()
    elif c.cube_contient_couleur('RU',2,5): # coin R bien placé
        if c.cube_contient_couleur('FU',3,5):
            mouvementsTemp = ('L','L','Ui','B','Fi','L','L','Bi','F','Ui','L','L')
            c.mouvements(mouvementsTemp) #on effectue les mouvements
            mouvementsTotal += mouvementsTemp
            mouvementsTemp = ()
        elif c.cube_contient_couleur('FU',4,5):
            mouvementsTemp = ('L','L','U','B','Fi','L','L','Bi','F','U','L','L')
            c.mouvements(mouvementsTemp) #on effectue les mouvements
            mouvementsTotal += mouvementsTemp
            mouvementsTemp = ()
    elif c.cube_contient_couleur('FU',1,5): # coin F bien placé
        if c.cube_contient_couleur('BU',2,5):
            mouvementsTemp = ('B','B','U','R','Li','B','B','Ri','L','U','B','B')
            c.mouvements(mouvementsTemp) #on effectue les mouvements
            mouvementsTotal += mouvementsTemp
            mouvementsTemp = ()
        elif c.cube_contient_couleur('BU',4,5):
            mouvementsTemp = ('B','B','Ui','R','Li','B','B','Ri','L','Ui','B','B')
            c.mouvements(mouvementsTemp) #on effectue les mouvements
            mouvementsTotal += mouvementsTemp
            mouvementsTemp = ()
    else:
        mouvementsTemp = ('F','F','U','L','Ri','F','F','Li','R','U','F','F')
        c.mouvements(mouvementsTemp)
        mouvementsTotal += mouvementsTemp
        mouvementsTemp = ()
        c, mouvementsTemp = pll(c) #besoin de relancer pll dessus
        mouvementsTotal += mouvementsTemp
        return c, mouvementsTotal

    return c, mouvementsTotal

if __name__ == '__main__':
    '''
    print("Test avec lecture d'entrée")
    b,c = lecture_cube('OGRBWYBGBGYYOYOWOWGRYOOOBGBRRYRBWWWRBWYGROWGRYBRGYWBOG')
    c0 = c.copy()
    print(c)
    print()
    print("CROSS")
    c,mouv = cross_facile(c)
    print(c)
    print("FIRST TWO LAYERS")
    c,mouv2 = ftl(c)
    print(c)
    print('Nombre de mouvements :', len(mouv+mouv2))
    print('Mouvements à effectuer :', mouv+mouv2)
    print()
    print("Test avec mouvements")
    #test OLL
    print("Test OLL avant")
    print(c)
    c, mouv3=oll(c)
    print("Test OLL")
    print(c)
    #test PLL
    print("Test PLL")
    c, mouv4 = pll(c)
    print(c)
    mouvements = mouv + mouv2 + mouv3 + mouv4
    validiteCfop = "OK" if cfop_valide(c0, mouvements) else "KO"
    '''

    from utils import TermColors
    tests = tableaux_test()# Fichier test
    i = 0
    moyennepll = 0
    for test in tests:
        i += 1
        c = Cube()
        c.scramble(test)
        c0 = c.copy()
        c, mouv = cross_facile(c)
        validiteCroix = "croix ok" if croix_valide(c) else "CROIX INVALIDE"
        c,mouv2 = ftl(c)
        validiteFtl = "ftl ok" if ftl_valide(c) else "FTL INVALIDE"
        c,mouv3=oll(c)
        validiteOll = "oll ok" if c.face_resolu('U') else "OLL INVALIDE"
        c,mouv4=pll(c)
        validitePll = "pll ok" if c.resolu() else "PLL INVALIDE"

        if not c.resolu():
            print("Le cube est insolvable")

        mouvements = mouv + mouv2 + mouv3 + mouv4
        validiteCfop = TermColors.bgGreen + "OK" + TermColors.end \
                        if cfop_valide(c0, mouvements) \
                        else TermColors.bgRed + "KO" + TermColors.end

        print(
            "{} {} ({}, {}, {}, {}) : {} mvts".format(
                validiteCfop, i, validiteCroix, validiteFtl, validiteOll, validitePll,
                len(mouvements)
            )
        )

    #Tests insolvabilité
    #Voir http://jeays.net/rubiks.htm#unsolvable

    tests = [
        #One edge piece is flipped in place and all other pieces are correct.
        'YYYOYYYYYOYOBBBRRRGGGOOOBBBRRRGGGOOOBBBRRRGGGWWWWWWWWW',
        #Two edge pieces need to be swapped and all other pieces are correct.
        'YYYYYYYYYOROBBBRORGGGOOOBBBRRRGGGOOOBBBRRRGGGWWWWWWWWW',
        #One corner piece needs rotating and all other pieces are correct.
        'OYYYYYYYYGOOBBBRRRGGYOOOBBBRRRGGGOOOBBBRRRGGGWWWWWWWWW',
        #Two corner pieces need to be swapped and all other pieces are correct.
        'YYYYYYYYYROOBBGORRGGBOOOBBBRRRGGGOOOBBBRRRGGGWWWWWWWWW'
    ]

    for t in tests:
        err, c = lecture_cube(t)
        assert(not err)

        err, _ = algo_cfop(c)
        print(TermColors.bgGreen + "Insolvable" + TermColors.end, c.to_line())

