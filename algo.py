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
        {Boolean|String}, Si le cube ne peut pas être résolu, renverra False
                          sinon, renverra une liste de String correspondant aux
                          différents mouvements à effectuer pour résoudre le cube
    '''

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

    mouvements1 = () #liste des mouvements à effectués part1
    mouvements2 = () #part2
    mouvements3 = () #part3
    mouvements4 = () #part4

    #On veut mettre l'arrête bleue-blanche à côté de la pièce centrale blanche
    #ie. la placer en FB jsute en dessous la pièce centrale bleue

    #On cherche l'arête bleue blanche
    if c.cube_contient_couleur('FU', 0, 1): #Si elle est sur la première couronne
        mouvements1 = ('F2',)
    elif c.cube_contient_couleur('RU', 0, 1):
        mouvements1 = ('U', 'F2')
    elif c.cube_contient_couleur('BU', 0, 1):
        mouvements1 = ('U2', 'F2')
    elif c.cube_contient_couleur('LU', 0, 1):
        mouvements1 = ('Ui', 'F2')

    elif c.cube_contient_couleur('FR', 0, 1): #Deuxième couronne
        mouvements1 = ('R', 'U', 'F2')
    elif c.cube_contient_couleur('BR', 0, 1):
        mouvements1 = ('Ri', 'U', 'F2')
    elif c.cube_contient_couleur('BL', 0, 1):
        mouvements1 = ('Bi', 'U2', 'F2')
    elif c.cube_contient_couleur('FL', 0, 1):
        mouvements1 = ('Fi',)

    elif c.cube_contient_couleur('LD', 0, 1): #Troisième couronne, autour du blanc
        mouvements1 = ('L2', 'Ui', 'F2')
    elif c.cube_contient_couleur('RD', 0, 1):
        mouvements1 = ('R2', 'U', 'F2')
    elif c.cube_contient_couleur('BD', 0, 1):
        mouvements1 = ('B2', 'U2', 'F2')

    if len(mouvements1) > 0:
        c.mouvements(mouvements1) #on effectue les mouvements

    #À ce niveau là, l'arrête bleue-blanche est au niveau de la troisième couronne
    #à l'endroit où il faut mais pas forcément paramétré comme il le faut: WWBB et pas WBWB

    if c.get_facette('FD', 0) != 1 : #Si pas bien paramétré,
                                     #il y a une suite de mouvements à effectuer
        mvtsFix = ('Fi', 'B', 'Ri', 'Di')
        c.mouvements(mvtsFix)
        mouvements1 += mvtsFix

    #La partie blanc-bleue est complétée

    #On fait pareil pour la partie orange

    if c.cube_contient_couleur('FU', 0, 4): #Si elle est sur la première couronne
        mouvements2 = ('U', 'L2')
    elif c.cube_contient_couleur('RU', 0, 4):
        mouvements2 = ('U2', 'L2')
    elif c.cube_contient_couleur('BU', 0, 4):
        mouvements2 = ('Ui', 'L2')
    elif c.cube_contient_couleur('LU', 0, 4):
        mouvements2 = ('L2',)

    elif c.cube_contient_couleur('FR', 0, 4): #Deuxième couronne
        mouvements2 = ('R', 'U2', 'L2')
    elif c.cube_contient_couleur('BR', 0, 4):
        mouvements2 = ('B', 'Ui', 'L2')
    elif c.cube_contient_couleur('BL', 0, 4):
        mouvements2 = ('Li',)
    elif c.cube_contient_couleur('FL', 0, 4):
        mouvements2 = ('L',)

    elif c.cube_contient_couleur('RD', 0, 4): #Troisième couronne, autour du blanc
        mouvements2 = ('R2', 'U2', 'L2')
    elif c.cube_contient_couleur('BD', 0, 4):
        mouvements2 = ('B2', 'Ui', 'L2')

    if len(mouvements2) > 0:
        c.mouvements(mouvements2) #on effectue les mouvements

    #A ce niveau là, l'arrête orange blanche est au niveau de la troisième couronne
    #à l'endroit où il faut mais pas forcément paramétré comme il le faut : WWOO et pas WOWO

    if c.get_facette('LD', 0) != 4 : #Si pas bien paramétré,
                                     #il y a une suite de mouvements à effectuer
        mvtsFix = ('Li', 'D', 'Fi', 'Di')
        c.mouvements(mvtsFix)
        mouvements2 += mvtsFix

    #La partie orange est complétée

    #On fait pareil pour la partie verte

    if c.cube_contient_couleur('FU', 0 ,3): #Si elle est sur la première couronne
        mouvements3 = ('U2', 'B2')
    elif c.cube_contient_couleur('RU', 0 ,3):
        mouvements3 = ('Ui', 'B2')
    elif c.cube_contient_couleur('BU', 0 ,3):
        mouvements3 = ('B2',)
    elif c.cube_contient_couleur('LU', 0 ,3):
        mouvements3 = ('U', 'B2')

    elif c.cube_contient_couleur('FR', 0 ,3): #Deuxième couronne
        mouvements3 = ('R', 'Ui', 'B2')
    elif c.cube_contient_couleur('BL', 0 ,3):
        mouvements3 = ('B',)
    elif c.cube_contient_couleur('BR', 0 ,3):
        mouvements3 = ('Bi',)
    elif c.cube_contient_couleur('FL', 0 ,3):
        mouvements3 = (
            'Li', 'U',
            'L', # Pour remettre la partie d'avant à sa place
            'B2'
        )

    elif c.cube_contient_couleur('RD', 0 ,3): #Troisième couronne, autour du blanc
        mouvements3 = ('R2', 'Ui', 'B2')

    if len(mouvements3) > 0:
        c.mouvements(mouvements3) #on effectue les mouvements

    #À ce niveau là, l'arrête verte blanche est au niveau de la troisième couronne
    #à l'endroit où il faut mais pas forcément paramétré comme il le faut : WWGG et pas WGWG

    if c.get_facette('BD', 0) != 3 : #Si pas bien paramétré,
                                     #il y a une suite de mouvements à effectuer
        mvtsFix = ('Bi', 'D', 'Li', 'Di')
        c.mouvements(mvtsFix)
        mouvements3 += mvtsFix

    #La partie verte est complétée

    #On fait pareil pour la partie rouge

    if c.cube_contient_couleur('FU', 0 ,2): #Si elle est sur la première couronne
        mouvements4 = ('Ui', 'R2')
    elif c.cube_contient_couleur('RU', 0 ,2):
        mouvements4 = ('R2',)
    elif c.cube_contient_couleur('BU', 0 ,2):
        mouvements4 = ('U', 'R2')
    elif c.cube_contient_couleur('LU', 0 ,2):
        mouvements4 = ('U2', 'R2')

    elif c.cube_contient_couleur('FR', 0 ,2): #Deuxième couronne
        mouvements4 = ('Ri',)
    elif c.cube_contient_couleur('BL', 0 ,2):
        mouvements4 = (
            'Bi', 'U',
            'B', # Pour remettre la partie d'avant à sa place
            'R2'
        )

    elif c.cube_contient_couleur('BR', 0 ,2):
        mouvements4 = ('R',)
    elif c.cube_contient_couleur('FL', 0 ,2):
        mouvements4 = ('F', 'Ui', 'Fi', 'R2')

    if len(mouvements4) > 0:
        c.mouvements(mouvements4) #on effectue les mouvements

    #A ce niveau là, l'arrête rouge blanche est au niveau de la troisième couronne
    #à l'endroit où il faut mais pas forcément paramétré comme il le faut : WWRR et pas WOWR

    if c.get_facette('RD', 0) != 2 : #Si pas bien paramétré,
                                     #il y a une suite de mouvements à effectuer
        mvtsFix = ('Ri', 'D', 'Bi', 'Di')
        c.mouvements(mvtsFix)
        mouvements4 += mvtsFix

    return c, mouvements1 + mouvements2 + mouvements3 + mouvements4

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
    else: # cube en down : pb chaque cas doit etre traité separement en fonction de ou est le cube bleu rouge
        if c.cube_contient_couleur('LU',1,2): # a gauche
            if c.cube_contient_couleur('LFD',0,1,2):
                mouvementsTemp = ('Ui','Li','Ui','L')
            elif c.cube_contient_couleur('RBD',0,1,2):
                mouvementsTemp = ('Ri','Ui','R','U2')
            elif c.cube_contient_couleur('BLD',0,1,2):
                mouvementsTemp = ('U','L','U2','Li')
        elif c.cube_contient_couleur('RU',1,2): # a droite
            if c.cube_contient_couleur('LFD',0,1,2):
                mouvementsTemp = ('Li','Ui','L')
            elif c.cube_contient_couleur('RBD',0,1,2):
                mouvementsTemp = ('Ri','Ui','R','U2')
            elif c.cube_contient_couleur('BLD',0,1,2):
                mouvementsTemp = ('L','U','Li','U')
        elif c.cube_contient_couleur('BU',1,2): # cube derriere
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
                    mouvementsTemp = ('R','U','Ri','U2','R','U','Ri','Ui','R','U','Ri') # 2*Ui = U2 ?
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
                    mouvementsTemp = ('U','Fi','Ui','F','Ui','R','U','Ri') # marche pas a priori
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
                    mouvementsTemp = ('Ui','Fi','U','F','U','Ri','Ui','R')
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
    # On initialise les listes de mouvements effectué que l'on donnent en sortie de fonction
    mouvements1 = ()
    mouvements2 = ()
    mouvements3 = ()

    # Test si on à pas déjà la croix
    if c.get_facette('FU',1)!=5 or c.get_facette('RU',1)!=5 \
        or c.get_facette('BU',1)!=5 or c.get_facette('LU',1)!=5:

        # Test de tout les cas possible
        if c.get_facette('FU',1)!=5 and c.get_facette('RU',1)!=5 \
            and c.get_facette('BU',1)!=5 and c.get_facette('LU',1)!=5:
            # Test si aucune des disposition, on fait une suite de rotation pour avoir un petit L ou une ligne
            mouvements1 = ('F','U','R','Ui','Ri','Fi')
            c.mouvements(mouvements1) # On effectue la liste de mouvements de la partie 1 (qui est optionnelle)

        #Cas ou on a une forme jaune en L sur la face du haut (U)

        # Test disposition en L n°1
        if c.get_facette('LU',1)==5 and c.get_facette('BU',1)==5 \
            and c.get_facette('FU',1)!=5 and c.get_facette('RU',1)!=5:
            mouvements2 = ('F','U','R','Ui','Ri','Fi')
        # Test disposition en L n°2
        elif c.get_facette('BU',1)==5 and c.get_facette('RU',1)==5 \
            and c.get_facette('LU',1)!=5 and c.get_facette('FU',1)!=5:
            mouvements2 = ('L','U','F','Ui','Fi','Li')
        # Test disposition en L n°3
        elif c.get_facette('RU',1)==5 and c.get_facette('FU',1)==5 \
            and c.get_facette('LU',1)!=5 and c.get_facette('BU',1)!=5:
            mouvements2 = ('B','U','L','Ui','Li','Bi')
        # Test disposition en L n°4
        elif c.get_facette('FU',1)==5 and c.get_facette('LU',1)==5 \
            and c.get_facette('BU',1)!=5 and c.get_facette('RU',1)!=5:
            mouvements2 = ('R','U','B','Ui','Bi','Ri')

        # Cas ou on à une ligne jaune sur la face du haut (U)

        # Test ligne n°1
        elif (c.get_facette('LU',1)==5 and c.get_facette('RU',1)==5 \
            and c.get_facette('BU',1)!=5 and c.get_facette('FU',1)!=5):
            mouvements2 = ('F','R','U','Ri','Ui','Fi')
        # Test ligne n°2
        elif c.get_facette('BU',1)==5 and c.get_facette('FU',1)==5 \
            and c.get_facette('RU',1)!=5 and c.get_facette('LU',1)!=5:
            mouvements2 = ('R','B','U','Bi','Ui','Ri')

        #On effectue la liste de mouvement de la partie 2
        c.mouvements(mouvements2)

    #Test de la croix jaune
    if c.get_facette('FU',1)==5 and c.get_facette('RU',1)==5 \
        and c.get_facette('BU',1)==5 and c.get_facette('LU',1)==5:

        #Cas numéro 1
        if (c.get_facette('FRU',0)==5 and c.get_facette('LFU',1)==5 \
            and c.get_facette('BLU',0)==5 and c.get_facette("RBU",1)):
            mouvements3 = ('R','U2','Ri','Ui','R','U','Ri','Ui','R','Ui','Ri')
        #cas numéro 1 : autre configration dans l'espace
        elif (c.get_facette('LFU',0)==5 and c.get_facette('BLU',1)==5\
            and c.get_facette('FRU',1)==5 and c.get_facette('RBU',0)==5):
            mouvements3 = ('B','U2','Bi','Ui','B','U','Bi','Ui','B','Ui','Bi')

        #cas numéro 2
        elif (c.get_facette('FRU',0)==5 and c.get_facette('LFU',0)==5\
            and c.get_facette('BLU',1)==5 and c.get_facette('RBU',1)==5):
            mouvements3 = ('R','U2','R2','Ui','R2','Ui','R2','U2','R')
        #Cas numéro 2 : autre configuration dans l'espace
        elif (c.get_facette('FRU',0)==5 and c.get_facette('LFU',1)==5\
            and c.get_facette('BLU',1)==5 and c.get_facette('RBU',0)==5):
            mouvements3 = ('B','U2','B2','Ui','B2','Ui','B2','U2','B')
        #Cas numéro 2 : autre configuration dans l'espace
        elif (c.get_facette('FRU',1)==5 and c.get_facette('LFU',1)==5\
            and c.get_facette('BLU',0)==5 and c.get_facette('RBU',0)==5):
            mouvements3 = ('L','U2','L2','Ui','L2','Ui','L2','U2','L')
        #Cas numéro 2 : autre configuration dans l'espace
        elif (c.get_facette('FRU',1)==5 and c.get_facette('LFU',0)==5\
            and c.get_facette('BLU',0)==5 and c.get_facette('RBU',1)==5):
            mouvements3 = ('F','U2','F2','Ui','F2','Ui','F2','U2','F')

        #Cas numéro 3
        elif (c.get_facette('LFU',2)==5 and c.get_facette('FRU',0)==5\
            and c.get_facette('FRU',2)!=5 and c.get_facette('BLU',2)!=5 \
            and c.get_facette('RBU',2)!=5):
            mouvements3 = ('R','U','Ri','U','R','U2','Ri')
        #Cas numéro 3 / autre disposition
        elif (c.get_facette('FRU',2)==5 and c.get_facette('RBU',0)==5\
            and c.get_facette('LFU',2)!=5 and c.get_facette('BLU',2)!=5 \
            and c.get_facette('RBU',2)!=5):
            mouvements3 = ('B','U','Bi','U','B','U2','Bi')
        #Cas numéro 3 / autre disposition
        elif (c.get_facette('RBU',2)==5 and c.get_facette('BLU',0)==5\
            and c.get_facette('FRU',2)!=5 and c.get_facette('LFU',2)!=5 \
            and c.get_facette('RBU',0)!=5):
            mouvements3 = ('L','U','Li','U','L','U2','Li')
        #Cas numéro 3 / autre disposition
        elif (c.get_facette('BLU',2)==5 and c.get_facette('LFU',0)==5\
            and c.get_facette('FRU',2)!=5 and c.get_facette('LFU',2)!=5 \
            and c.get_facette('RBU',2)!=5):
            mouvements3 = ('F','U','Fi','U','F','U2','Fi')

        #Cas numéro 4
        elif (c.get_facette('RBU',2)==5 and c.get_facette('BLU',2)!=5\
            and c.get_facette('FRU',2)!=5 and c.get_facette('LFU',2)!=5\
            and c.get_facette('BLU',0)!=5):
            mouvements3 = ('R','U2','Ri','Ui','R','Ui','Ri')
        #Cas numéro 4 / autre disposition
        elif (c.get_facette('BLU',2)==5 and c.get_facette('LFU',2)!=5\
            and c.get_facette('FRU',2)!=5 and c.get_facette('RBU',2)!=5\
            and c.get_facette('LFU',0)!=5):
            mouvements3 = ('B','U2','Bi','Ui','B','Ui','Bi')
        #Cas numéro 4 / autre disposition
        elif (c.get_facette('LFU',2)==5 and c.get_facette('FRU',2)!=5\
            and c.get_facette('RBU',2)!=5 and c.get_facette('BLU',2)!=5\
            and c.get_facette('FRU',0)!=5):
            mouvements3 = ('L','U2','Li','Ui','L','Ui','Li')
        #Cas numéro 4 / autre disposition
        elif (c.get_facette('FRU',2)==5 and c.get_facette('RBU',2)!=5\
            and c.get_facette('LFU',2)!=5 and c.get_facette('BLU',2)!=5\
            and c.get_facette('RBU',0)!=5):
            mouvements3 = ('F','U2','Fi','Ui','F','Ui','Fi')

        #Cas numéro 5
        elif (c.get_facette('FRU',0)==5 and c.get_facette('LFU',1)==5\
            and c.get_facette('BLU',2)==5 and c.get_facette('RBU',2)==5):
            mouvements3 = ('R2','D','Ri','U2','R','Di','Ri','U2','Ri')
        #Cas numéro 5 / autre disposition
        elif (c.get_facette('FRU',1)==5 and c.get_facette('LFU',2)==5\
            and c.get_facette('BLU',2)==5 and c.get_facette('RBU',0)==5):
            mouvements3 = ('B2','D','Bi','U2','B','Di','Bi','U2','Bi')
        #Cas numéro 5 / autre disposition
        elif (c.get_facette('FRU',2)==5 and c.get_facette('LFU',2)==5\
            and c.get_facette('BLU',0)==5 and c.get_facette('RBU',1)==5):
            mouvements3 = ('L2','D','Li','U2','L','Di','Li','U2','Li')
        #Cas numéro 5 / autre disposition
        elif (c.get_facette('FRU',2)==5 and c.get_facette('LFU',0)==5\
            and c.get_facette('BLU',1)==5 and c.get_facette('RBU',2)==5):
            mouvements3 = ('F2','D','Fi','U2','F','Di','Fi','U2','Fi')

        #Cas numéro 6
        elif (c.get_facette('FRU',2)==5 and c.get_facette('LFU',1)==5\
            and c.get_facette('BLU',0)==5 and c.get_facette('RBU',2)==5):
            mouvements3 = ('L','F','Ri','Fi','Li','F','R','Fi')
        #Cas numéro 6 / autre disposition
        elif (c.get_facette('FRU',1)==5 and c.get_facette('LFU',0)==5\
            and c.get_facette('BLU',2)==5 and c.get_facette('RBU',2)==5):
            mouvements3 = ('F','R','Bi','Ri','Fi','R','B','Ri')
        #Cas numéro 6 / autre disposition
        elif (c.get_facette('FRU',0)==5 and c.get_facette('LFU',2)==5\
            and c.get_facette('BLU',2)==5 and c.get_facette('RBU',1)==5):
            mouvements3 = ('R','B','Li','Bi','Ri','B','L','Bi')
        #Cas numéro 6 / autre disposition
        elif (c.get_facette('FRU',2)==5 and c.get_facette('LFU',2)==5\
            and c.get_facette('BLU',1)==5 and c.get_facette('RBU',0)==5):
            mouvements3 = ('B','L','Fi','Li','Bi','L','F','Li')

        #Cas numéro 7
        elif (c.get_facette('FRU',0)==5 and c.get_facette('LFU',2)==5\
            and c.get_facette('RBU',2)==5 and c.get_facette('BLU',1)==5):
            mouvements3 = ('Fi','L','F','Ri','Fi','Li','F','R')
        #Cas numéro 7 / autre disposition
        elif (c.get_facette('FRU',2)==5 and c.get_facette('LFU',1)==5\
            and c.get_facette('BLU',2)==5 and c.get_facette('RBU',0)==5):
            mouvements3 = ('Ri','F','R','Bi','Ri','Fi','R','B')
        #Cas numéro 7 / autre disposition
        elif (c.get_facette('FRU',1)==5 and c.get_facette('LFU',2)==5\
            and c.get_facette('BLU',0)==5 and c.get_facette('RBU',2)==5):
            mouvements3 = ('Bi','R','B','Li','Bi','Ri','B','L')
        #Cas numéro 7 / autre disposition
        elif (c.get_facette('FRU',2)==5 and c.get_facette('LFU',0)==5\
            and c.get_facette('BLU',2)==5 and c.get_facette('RBU',1)==5):
            mouvements3 = ('Li','B','L','Fi','Li','Bi','L','F')
        c.mouvements(mouvements3)

    return c, mouvements1 + mouvements2 + mouvements3

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

    mouvements1 = ()    #liste des mouvements à effectués part1
    mouvements2 = ()    #part2
    mouvements3 = ()    #part3
    mouvements4 = ()    #part4
    mvtsFix = ()

    #On place correctement les coins du haut
    while not ((c.cube_contient_couleur('BLU',3,4,5) and c.cube_contient_couleur('RBU',2,3,5))
        or (c.cube_contient_couleur('RBU',2,3,5) and c.cube_contient_couleur('FRU',1,2,5))
        or (c.cube_contient_couleur('FRU',1,2,5) and c.cube_contient_couleur('LFU',4,1,5))
        or (c.cube_contient_couleur('LFU',4,1,5) and c.cube_contient_couleur('BLU',3,4,5))
        or (c.cube_contient_couleur('BLU',3,4,5) and c.cube_contient_couleur('FRU',1,2,5))
        or (c.cube_contient_couleur('RBU',2,3,5) and c.cube_contient_couleur('LFU',4,1,5))):
        mvtsFix = ('U',)
        c.mouvements(mvtsFix)
        mouvements1 += mvtsFix

    mvtsFix = ()

    if c.cube_contient_couleur('BLU',3,4,5) \
        and c.cube_contient_couleur('RBU',2,3,5) \
        and c.cube_contient_couleur('FRU',1,2,5) \
        and c.cube_contient_couleur('LFU',4,1,5):
            pass #les 4 Coins sont déjà bien placés
    #Coins bien placés au fond
    elif c.cube_contient_couleur('BLU',3,4,5) and c.cube_contient_couleur('RBU',2,3,5):
        mouvements2 = ('Ri','F','Ri','B','B','R','Fi','Ri','B','B','R','R','Ui')
    #Coins biens placés à droite
    elif c.cube_contient_couleur('RBU',2,3,5) and c.cube_contient_couleur('FRU',1,2,5):
        mouvements2 = ('Fi','L','Fi','R','R','F','Li','Fi','R','R','F','F','Ui')
    #Coins bien placés devant
    elif c.cube_contient_couleur('FRU',1,2,5) and c.cube_contient_couleur('LFU',4,1,5):
        mouvements2 = ('Li','B','Li','F','F','L','Bi','Li','F','F','L','L','Ui')
    #Coins bien placés à gauche
    elif c.cube_contient_couleur('LFU',4,1,5) and c.cube_contient_couleur('BLU',3,4,5):
        mouvements2 = ('Bi','R','Bi','L','L','B','Ri','Bi','L','L','B','B','Ui')
    #coins bien placés en diagonale #1
    elif c.cube_contient_couleur('BLU',3,4,5) and c.cube_contient_couleur('FRU',1,2,5):
        mouvements2 = ('Ri','F','Ri','B','B','R','Fi','Ri','B','B','R','R','Ui')
        c.mouvements(mouvements2)
        c, mouvements3 = pll(c) #on a besoin de rappeller pll dessus
        return c, mouvements1 + mouvements2 + mouvements3
    #coins bien placés en diagonale #2
    elif c.cube_contient_couleur('RBU',2,3,5) and c.cube_contient_couleur('LFU',4,1,5):
        mouvements2 = ('Ri','F','Ri','B','B','R','Fi','Ri','B','B','R','R','Ui')
        c.mouvements(mouvements2)
        c, mouvements3 = pll(c) #on a besoin de rappeller pll dessus
        return c, mouvements1 + mouvements2 + mouvements3

    if len(mouvements2) > 0:
        c.mouvements(mouvements2) #on effectue les mouvements

    #on positionne maintenant les arêtes jaunes
    mouvements3 = ()

    if c.cube_contient_couleur('LU',4,5):
        while not (c.cube_contient_couleur('FU',1,5)
            and c.cube_contient_couleur('RU',2,5)
            and c.cube_contient_couleur('BU',3,5)):
            mvts = ('R','R','U','F','Bi','R','R','Fi','B','U','R','R')
            c.mouvements(mvts)
            mouvements3 += mvts

    elif c.cube_contient_couleur('BU',3,5):
        while not (c.cube_contient_couleur('FU',1,5)
            and c.cube_contient_couleur('RU',2,5)
            and c.cube_contient_couleur('LU',4,5)):
            mvts = ('F','F','U','L','Ri','F','F','Li','R','U','F','F')
            c.mouvements(mvts)
            mouvements3 += mvts

    elif c.cube_contient_couleur('RU',2,5):
        while not (c.cube_contient_couleur('FU',1,5)
            and c.cube_contient_couleur('LU',4,5)
            and c.cube_contient_couleur('BU',3,5)):
            mvts = ('L','L','U','B','Fi','L','L','Bi','F','U','L','L')
            c.mouvements(mvts)
            mouvements3 += mvts

    elif c.cube_contient_couleur('FU',1,5):
        while not (c.cube_contient_couleur('LU',4,5)
            and c.cube_contient_couleur('RU',2,5)
            and c.cube_contient_couleur('BU',3,5)):
            mvts = ('B','B','U','R','Li','B','B','Ri','L','U','B','B')
            c.mouvements(mvts)
            mouvements3 += mvts

    else:
        mouvements3 = ('F','F','U','L','Ri','F','F','Li','R','U','F','F')
        c.mouvements(mouvements3)
        c, mouvements4 = pll(c) #besoin de relancer pll dessus
        return c, mouvements1 + mouvements2 + mouvements3 + mouvements4

    return c, mouvements1 + mouvements2 + mouvements3

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

    tests = tableaux_test()# Fichier test
    i = 0
    somme = 0
    testValide = 0
    for test in tests:
        i += 1
        c = Cube()
        c.scramble(test)
        c0 = c.copy()
        c, mouv = cross_facile(c)
        validiteCroix = "croix ok" if croix_valide(c) else "CROIX INVALIDE"
        c,mouv2 = ftl(c)
        if c.cube_contient_couleur('FRD',0,1,2) and c.cube_contient_couleur('FR',1,2):
            validiteFtl = "ftl ok"
            somme += len(mouv2)
            testValide += 1
        else:
            validiteFtl = "FTL INVALIDE"
        print ("Test "+str(i)+" : "+validiteCroix+" "+validiteFtl+" "+str(len(mouv2)))
    print("Moyenne : "+str(somme/testValide))
