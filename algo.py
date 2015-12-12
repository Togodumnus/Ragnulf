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
from utils import croix_valide, ftl_valide
from test import tableaux_test


def algo_cfop(c):
    '''
    algo

    Prend le cube en entrée, et avec l'algo de résolution choisi,
    va déterminer la suite de mouvements qu'il faut réaliser pour résoudre le cube

    :Args:
        c {Cube}    l'objet cube, à résoudre

    :Returns:
        {Boolean|String}    si le cube ne peut pas être résolu, renverra False
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

    c2 = Cube()
    mouvements1 = () #liste des mouvements à effectués part1
    mouvements2 = () #part2
    mouvements3 = () #part3
    mouvements4 = () #part4
    mouvements5 = () #part5
    mouvements6 = () #part6
    mouvements7 = () #part7
    mouvements8 = () #part8
    mouvements9 = () #part9
    mouvements10 = () #part10
    mouvements11 = () #part11
    mouvements12 = () #part12
    mouvements13 = () #part13
    mouvements14 = () #part14
    mouvements15 = () #part15
    mouvements16 = () #part16
    mvtsFix = ()

    # Cube Bleu Orange Blanche
    # On le place d'abord en LFU

    # cube bien placé
    if c.cube_contient_couleur('LFD',0,1,4) and c.get_facette('LFD',0)==4:
        pass
    else:
        # cube bien placé mais pas bien orienté
        if c.cube_contient_couleur('LFD',0,1,4) and c.get_facette('LFD',0)!=4:
            mouvements1 = ('Li','Ui','L','U')
        elif c.cube_contient_couleur('LFU',0,1,4):
            pass
        elif c.cube_contient_couleur('FRD',0,1,4):
            mouvements1 = ('R', 'U','Ri')
        elif c.cube_contient_couleur('FRU',0,1,4):
            mouvements1 = ('U',)
        elif c.cube_contient_couleur('RBU',0,1,4):
            mouvements1 = ('U2',)
        elif c.cube_contient_couleur('RBD',0,1,4):
            mouvements1 = ('Ri','U2','R')
        elif c.cube_contient_couleur('BLD',0,1,4):
            mouvements1 = ('L','U2','Li','U')
        elif c.cube_contient_couleur('BLU',0,1,4):
            mouvements1 = ('Ui',)

        if len(mouvements1) > 0:
            c.mouvements(mouvements1) #on effectue les mouvements

        # Puis on place bien le cube
        if c.get_facette('LFU',2)==0:
            mvtsFix = ('Li','U2','L','U')
            c.mouvements(mvtsFix)
        else:
            mvtsFix = ()

        if c.get_facette('LFU',0)==0:
            mouvements2 = ('Fi','L','F','Li')
        elif c.get_facette('LFU',0)==4:
            mouvements2 = ('L','Fi','Li','F')

        if len(mouvements2) > 0:
            c.mouvements(mouvements2) #on effectue les mouvements
            mouvements2 += mvtsFix

    # Cube Bleu Rouge Blanche
    # On cherche d'abord à mettre le cube en FRU

    # cube bien placé et orienté
    if c.cube_contient_couleur('FRD',0,1,2) and c.get_facette('FRD',0)==1:
        pass
    else:
        # cube bien placé mais pas bien orienté
        if c.cube_contient_couleur('FRD',0,1,2) :
            mouvements3 = ('R','U','Ri','Ui')
        elif c.cube_contient_couleur('FRU',0,1,2):
            pass
        elif c.cube_contient_couleur('LFU',0,1,2):
            mouvements3 = ('Ui',)
        elif c.cube_contient_couleur('RBU',0,1,2):
            mouvements3 = ('U',)
        elif c.cube_contient_couleur('RBD',0,1,2):
            mouvements3 = ('Ri','U2','R','Ui')
        elif c.cube_contient_couleur('BLD',0,1,2):
            mouvements3 = ('L','U2','Li')
        elif c.cube_contient_couleur('BLU',0,1,2):
            mouvements3 = ('U2',)

        if len(mouvements3) > 0:
            c.mouvements(mouvements3) #on effectue les mouvements

        # On place ensuite bien le cube en FRD
        if c.get_facette('FRU',2)==0:
            mvtsFix = ('Fi','U2','F','U')
            c.mouvements(mvtsFix)
        else:
            mvtsFix = ()

        if c.get_facette('FRU',1)==0:
            mouvements4 = ('F','Ri','Fi','R')
        elif c.get_facette('FRU',1)==2:
            mouvements4 = ('Ri','F','R','Fi')

        if len(mouvements4) > 0:
            c.mouvements(mouvements4) #on effectue les mouvements
            mouvements4 += mvtsFix


    # Vert orange
    # On cherche à le mettre en BLU
    if c.cube_contient_couleur('BLD',0,3,4) and c.get_facette('BLD',2)==0:
        pass
    else:
        if c.cube_contient_couleur('BLD',0,3,4):
            mouvements5 = ('L','U','Li','Ui')
        elif c.cube_contient_couleur('FRU',0,3,4):
            mouvements5 = ('U2',)
        elif c.cube_contient_couleur('RBU',0,3,4):
            mouvements5 = ('Ui',)
        elif c.cube_contient_couleur('RBD',0,3,4):
            mouvements5 = ('Ri','Ui','R')
        elif c.cube_contient_couleur('BLU',0,3,4):
            pass
        elif c.cube_contient_couleur('LFU',0,3,4):
            mouvements5 = ('U',)

        if len(mouvements5) > 0:
            c.mouvements(mouvements5) #on effectue les mouvements

        # On place ensuite bien le cube en BLD
        if c.get_facette('BLU',2)==0:
            mvtsFix = ('Bi','U2','B','U')
            c.mouvements(mvtsFix)
        else:
            mvtsFix = ()

        if c.get_facette('BLU',0)==0:
            mouvements6 = ('Li','B','L','Bi')
        elif c.get_facette('BLU',0)==3:
            mouvements6 = ('B','Li','Bi','L')

        if len(mouvements6) > 0:
            c.mouvements(mouvements6) #on effectue les mouvements
            mouvements6 += mvtsFix

    # Vert rouge
    # On cherche à le mettre en RBU
    if c.cube_contient_couleur('RBD',0,2,3) and c.get_facette('RBD',2)==0:
        pass
    else:
        if c.cube_contient_couleur('RBD',0,2,3):
            mouvements7 = ('Ri','Ui','R','U')
        elif c.cube_contient_couleur('FRU',0,2,3):
            mouvements7 = ('Ui',)
        elif c.cube_contient_couleur('RBU',0,2,3):
            pass
        elif c.cube_contient_couleur('BLU',0,2,3):
            mouvements7= ('U',)
        elif c.cube_contient_couleur('LFU',0,2,3):
            mouvements7 = ('U2',)

        if len(mouvements7) > 0:
            c.mouvements(mouvements7) #on effectue les mouvements

        # On place ensuite bien le cube en RBD
        if c.get_facette('RBU',2)==0:
            mvtsFix = ('Ri','U2','R','U')
            c.mouvements(mvtsFix)
        else:
            mvtsFix = ()

        if c.get_facette('RBU',1)==0:
            mouvements8 = ('R','Bi','Ri','B')
        elif c.get_facette('RBU',1)==3:
            mouvements8 = ('Bi','R','B','Ri')

        if len(mouvements8) > 0:
            c.mouvements(mouvements8) #on effectue les mouvements
            mouvements8 += mvtsFix

    #####################
    # Deuxième couronne #
    #####################

    # Vert Rouge

    if c.cube_contient_couleur('BR',3,2) and c.get_facette('BR',0)==3:
        pass # cube deja bien mis
    else:
        if c.cube_contient_couleur('BR',3,2):
            mouvements9 = ('Ri','U','R','U','B','Ui','Bi') # on enlève la pièce
        elif c.cube_contient_couleur('FR',3,2):
            mouvements9 = ('R','Ui','Ri','Ui','Fi','U','F') # on enlève la pièce
        elif c.cube_contient_couleur('FL',3,2):
            mouvements9 = ('Li','U','L','U','F','Ui','Fi') # on enlève la pièce
        elif c.cube_contient_couleur('BL',3,2):
            mouvements9 = ('L','Ui','Li','Ui','Bi','U','B') # on enlève la pièce

        if len(mouvements9) > 0:
            c.mouvements(mouvements9) #on effectue les mouvements

        if c.cube_contient_couleur('FU',3,2):
            if c.get_facette('FU',0)==2:
                mouvements10 = ('B','Ui','Bi','Ui','Ri','U','R')
            elif c.get_facette('FU',0)==3:
                mouvements10 = ('U','Ri','U','R','U','B','Ui','Bi')
        elif c.cube_contient_couleur('RU',3,2):
            if c.get_facette('RU',0)==2:
                mouvements10 = ('U','B','Ui','Bi','Ui','Ri','U','R')
            elif c.get_facette('RU',0)==3:
                mouvements10 = ('U2','Ri','U','R','U','B','Ui','Bi')
        elif c.cube_contient_couleur('LU',3,2):
            if c.get_facette('LU',0)==2:
                mouvements10 = ('Ui','B','Ui','Bi','Ui','Ri','U','R')
            elif c.get_facette('LU',0)==3:
                mouvements10 = ('Ri','U','R','U','B','Ui','Bi')
        elif c.cube_contient_couleur('BU',3,2):
            if c.get_facette('BU',0)==2:
                mouvements10 = ('U2','B','Ui','Bi','Ui','Ri','U','R')
            elif c.get_facette('BU',0)==3:
                mouvements10 = ('Ui','Ri','U','R','U','B','Ui','Bi')

    if len(mouvements10) > 0:
        c.mouvements(mouvements10) #on effectue les mouvements

    # Face Orange Vert
    if c.cube_contient_couleur('BL',3,4) and c.get_facette('BL',0)==3:
        pass # cube deja bien mis
    else:
        if c.cube_contient_couleur('FR',3,4):
            mouvements11 = ('R','Ui','Ri','Ui','Fi','U','F') # on enlève la pièce
        elif c.cube_contient_couleur('FL',3,4):
            mouvements11 = ('Li','U','L','U','F','Ui','Fi') # on enlève la pièce
        elif c.cube_contient_couleur('BL',3,4):
            mouvements11 = ('L','Ui','Li','Ui','Bi','U','B') # on enlève la pièce

    if len(mouvements11) > 0:
        c.mouvements(mouvements11) #on effectue les mouvements

    if c.cube_contient_couleur('FU',3,4):
        if c.get_facette('FU',0)==3:
            mouvements12 = ('Ui','L','Ui','Li','Ui','Bi','U','B')
        elif c.get_facette('FU',0)==4:
            mouvements12 = ('Bi','U','B','U','L','Ui','Li')
    elif c.cube_contient_couleur('RU',3,4):
        if c.get_facette('RU',0)==3:
            mouvements12 = ('L','Ui','Li','Ui','Bi','U','B')
        elif c.get_facette('RU',0)==4:
            mouvements12 = ('U','Bi','U','B','U','L','Ui','Li')
    elif c.cube_contient_couleur('LU',3,4):
        if c.get_facette('LU',0)==3:
            mouvements12 = ('U2','L','Ui','Li','Ui','Bi','U','B')
        elif c.get_facette('LU',0)==4:
            mouvements12 = ('Ui','Bi','U','B','U','L','Ui','Li')
    elif c.cube_contient_couleur('BU',3,4):
        if c.get_facette('BU',0)==3:
            mouvements12 = ('U','L','Ui','Li','Ui','Bi','U','B')
        elif c.get_facette('BU',0)==4:
            mouvements12 = ('U2','Bi','U','B','U','L','Ui','Li')

    if len(mouvements12) > 0:
        c.mouvements(mouvements12) #on effectue les mouvements

    # Bleu Orange
    if c.cube_contient_couleur('FL',1,4) and c.get_facette('FL',0)==1:
        pass # cube deja bien mis
    else:
        if c.cube_contient_couleur('FR',1,4):
            mouvements13 = ('R','Ui','Ri','Ui','Fi','U','F') # on enlève la pièce
        elif c.cube_contient_couleur('FL',1,4):
            mouvements13 = ('Li','U','L','U','F','Ui','Fi') # on enlève la pièce

    if len(mouvements13) > 0:
        c.mouvements(mouvements13) #on effectue les mouvements

    if c.cube_contient_couleur('FU',1,4):
        if c.get_facette('FU',0)==4:
            mouvements14 = ('U2','F','Ui','Fi','Ui','Li','U','L')
        elif c.get_facette('FU',0)==1:
            mouvements14 = ('Ui','Li','U','L','U','F','Ui','Fi')
    elif c.cube_contient_couleur('RU',1,4):
        if c.get_facette('RU',0)==4:
            mouvements14 = ('Ui','F','Ui','Fi','Ui','Li','U','L')
        elif c.get_facette('RU',0)==1:
            mouvements14 = ('Li','U','L','U','F','Ui','Fi')
    elif c.cube_contient_couleur('LU',1,4):
        if c.get_facette('LU',0)==4:
            mouvements14 = ('U','F','Ui','Fi','Ui','Li','U','L')
        elif c.get_facette('LU',0)==1:
            mouvements14 = ('U2','Li','U','L','U','F','Ui','Fi')
    elif c.cube_contient_couleur('BU',1,4):
        if c.get_facette('BU',0)==4:
            mouvements14 = ('F','Ui','Fi','Ui','Li','U','L')
        elif c.get_facette('BU',0)==1:
            mouvements14 = ('U','Li','U','L','U','F','Ui','Fi')

    if len(mouvements14) > 0:
        c.mouvements(mouvements14) #on effectue les mouvements

    # Rouge bleu
    if c.cube_contient_couleur('FR',1,2) and c.get_facette('FR',0)==1:
        pass # cube deja bien mis
    elif c.cube_contient_couleur('FR',1,2) and c.get_facette('FR',0)==2:
        mouvements15 = ('R','Ui','Ri','Ui','Fi','U','F') # on enlève la pièce

    if len(mouvements15) > 0:
        c.mouvements(mouvements15) #on effectue les mouvements

    if c.cube_contient_couleur('FU',1,2):
        if c.get_facette('FU',0)==1:
            mouvements16 = ('U','R','Ui','Ri','Ui','Fi','U','F')
        elif c.get_facette('FU',0)==2:
            mouvements16 = ('U2','Fi','U','F','U','R','Ui','Ri')
    elif c.cube_contient_couleur('RU',1,2):
        if c.get_facette('RU',0)==1:
            mouvements16 = ('U2','R','Ui','Ri','Ui','Fi','U','F')
        elif c.get_facette('RU',0)==2:
            mouvements16 = ('Ui','Fi','U','F','U','R','Ui','Ri')
    elif c.cube_contient_couleur('LU',1,2):
        if c.get_facette('LU',0)==1:
            mouvements16 = ('R','Ui','Ri','Ui','Fi','U','F')
        elif c.get_facette('LU',0)==2:
            mouvements16 = ('U','Fi','U','F','U','R','Ui','Ri')
    elif c.cube_contient_couleur('BU',1,2):
        if c.get_facette('BU',0)==1:
            mouvements16 = ('Ui','R','Ui','Ri','Ui','Fi','U','F')
        elif c.get_facette('BU',0)==2:
            mouvements16 = ('Fi','U','F','U','R','Ui','Ri')

    if len(mouvements16) > 0:
        c.mouvements(mouvements16) #on effectue les mouvements


    # Traiter le cas ou le cube n'est pas dans le bon sens
    # Et lorsque le cube est sur un coté

    return c, mouvements1 + mouvements2 + mouvements3 + mouvements4 \
            + mouvements5 + mouvements6 + mouvements7 + mouvements8 \
            + mouvements9 + mouvements10 + mouvements11 + mouvements12 \
            + mouvements13 + mouvements14 + mouvements15 + mouvements16

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

        i = 0 #On initiaise i
        while i < 3: #Jusqu'à trois boucle au plus pour résoudre la face jaune

            #On initialise mouvementsBoucle qui effectue les mouvement à chaque tour de boucle
            mouvementsBoucle = ()

            #Si la face jaune n'est pas résolue
            if not c.face_resolu('U'):

                # Cas ou on n'a aucun coins jaune sur la face du dessus (U)
                if c.get_facette('LFU',2) != 5 and c.get_facette('RBU',2) != 5 \
                    and c.get_facette('BLU',2) != 5 and c.get_facette('FRU',2) !=5:

                    #Il faut repérer les coins jaune sur la troisième couronne, ici en LFU 0
                    if c.get_facette('LFU',0) == 5:
                        mouvementsBoucle += ('R','U','Ri','U','R','U2','Ri')
                    # Coin jaune en BLU 0 sur la troisième couronne
                    elif c.get_facette('BLU',0) == 5:
                        mouvementsBoucle += ('F','U','Fi','U','F','U2','Fi')
                    # Coin jaune en RBU 0 sur la troisième couronne
                    elif c.get_facette('RBU',0) == 5:
                        mouvementsBoucle += ('L','U','Li','U','L','U2','Li')
                    # Coin jaune en FRU 0 sur la troisième couronne
                    elif c.get_facette('FRU',0) == 5:
                        mouvementsBoucle += ('B','U','Bi','U','B','U2','Bi')

                # Cas ou on à 1 seul coins jaune sur la face du haut (U) en bas à gauche
                elif c.get_facette('LFU',2) == 5 and c.get_facette('RBU',2) != 5 \
                    and c.get_facette('BLU',2) != 5 and c.get_facette('FRU',2) !=5:
                    mouvementsBoucle += ('R','U','Ri','U','R','U2','Ri')
                # Cas ou on à 1 seul coins jaune sur la face du haut (U) en haut à gauche
                elif c.get_facette('RBU',2) == 5 and c.get_facette('LFU',2) != 5 \
                    and c.get_facette('BLU',2) != 5 and c.get_facette('FRU',2) !=5:
                    mouvementsBoucle += ('L','U','Li','U','L','U2','Li')
                # Cas ou on à 1 seul coins jaune sur la face du haut (U) en haut à droite
                elif c.get_facette('BLU',2) == 5 and c.get_facette('RBU',2) != 5 \
                    and c.get_facette('LFU',2) != 5 and c.get_facette('FRU',2) !=5:
                    mouvementsBoucle += ('F','U','Fi','U','F','U2','Fi')
                # Cas ou on à 1 seul coins jaune sur la face du haut (U) en bas à droite
                elif c.get_facette('FRU',2) == 5 and c.get_facette('RBU',2) != 5 \
                    and c.get_facette('BLU',2) != 5 and c.get_facette('LFU',2) !=5:
                    mouvementsBoucle += ('B','U','Bi','U','B','U2','Bi')

                #Cas ou on à plus de 2 coins jaune sur la face du haut (U),
                #on ne prend pas en compte le placement de ces coins
                else: #On à forcément au moins deux coins
                    if c.get_facette('LFU',1) == 5:
                        mouvementsBoucle += ('R','U','Ri','U','R','U2','Ri')
                    if c.get_facette('BLU',1) == 5:
                        mouvementsBoucle += ('F','U','Fi','U','F','U2','Fi')
                    if c.get_facette('FRU',1) == 5:
                        mouvementsBoucle += ('B','U','Bi','U','B','U2','Bi')
                    if c.get_facette('RBU',1) == 5:
                        mouvementsBoucle += ('L','U','Li','U','L','U2','Li')

            c.mouvements(mouvementsBoucle) # On effectue les mouvements
            mouvements3 += mouvementsBoucle # On concatène les mouvement à ceux de la partie 3

            i += 1 # On incrémente le compteur de boucle

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

    mouvements1 = () #liste des mouvements à effectués part1
    mouvements2 = () #part2
    mouvements3 = () #part3
    mouvements4 = () #part4
    mouvements5 = () #part5
    mouvements6 = () #part6
    mouvements7 = () #part7
    mouvements8 = () #part8
    mouvements9 = () #part8
    mouvements10 = () #part8
    mouvements11= () #part8
    mouvements12 = () #part8
    mvtsFix = ()

    # On place correctement les coins jaunes

    while not ((c.cube_contient_couleur('BLU',3,4,5) and c.cube_contient_couleur('RBU',2,3,5))
        or (c.cube_contient_couleur('RBU',2,3,5) and c.cube_contient_couleur('FRU',1,2,5))
        or (c.cube_contient_couleur('FRU',1,2,5) and c.cube_contient_couleur('LFU',4,1,5))
        or (c.cube_contient_couleur('LFU',4,1,5) and c.cube_contient_couleur('BLU',3,4,5))
        or (c.cube_contient_couleur('BLU',3,4,5) and c.cube_contient_couleur('FRU',1,2,5))
        or (c.cube_contient_couleur('RBU',2,3,5) and c.cube_contient_couleur('LFU',4,1,5))):
        mvtsFix = ('U',)
        c.mouvements(mvtsFix)
        mouvements1 += mvtsFix

    mvtsFix = () # On remet à 0 notre tableau de mouvements Fix

    #Coins bien placés au fond
    if c.cube_contient_couleur('BLU',3,4,5) and c.cube_contient_couleur('RBU',2,3,5):
        mouvements2 = ('Ri','F','Ri','B','B','R','Fi','Ri','B','B','R','R','Ui')
    #Coins biens placés à droite
    elif c.cube_contient_couleur('RBU',2,3,5) and c.cube_contient_couleur('FRU',1,2,5):
        mouvements2 = ('Fi','L','F','R','R','F','Li','Fi','R','R','F','F','Ui')
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
        return pll(c)
    #coins bien placés en diagonale #2
    elif cube_contient_couleur('RBU',2,3,5) and c.cube_contient_couleur('LFU',4,1,5):
        mouvements2 = ('Ri','F','Ri','B','B','R','Fi','Ri','B','B','R','R','Ui')
        c.mouvements(mouvements2)
        return pll(c)

    elif c.cube_contient_couleur('BLU',3,4,5) and c.cube_contient_couleur('RBU',2,3,5) \
        and c.cube_contient_couleur('FRU',1,2,5) and c.cube_contient_couleur('LFU',4,1,5):
         pass #les 4 Coins sont déjà bien placés

    if len(mouvements2) > 0:
        c.mouvements(mouvements2) #on effectue les mouvements

        #on positionne maintenant les arêtes jaunes
        if c.cube_contient_couleur('LU',4,5):
            while not (c.cube_contient_couleur('FU',1,5)
                and c.cube_contient_couleur('RU',2,5)
                and c.cube_contient_couleur('BU',3,5)):
                mouvements3 = ('R','R','U','F','Bi','R','R','Fi','B','U','R','R')
                c.mouvements(mouvements3)
        elif c.cube_contient_couleur('BU',3,5):
            while not (c.cube_contient_couleur('FU',1,5)
                and c.cube_contient_couleur('RU',2,5)
                and c.cube_contient_couleur('BU',3,5)):
                mouvements3 = ('F','F','U','L','Ri','F','F','Li','R','U','F','F')
                c.mouvements(mouvements3)
        elif c.cube_contient_couleur('RU',2,5):
            while not (c.cube_contient_couleur('FU',1,5)
                and c.cube_contient_couleur('RU',2,5)
                and c.cube_contient_couleur('BU',3,5)):
                mouvements3 = ('L','L','U','B','Fi','L','L','Bi','F','U','L','L')
                c.mouvements(mouvements3)
        elif c.cube_contient_couleur('FU',1,5):
            while not (c.cube_contient_couleur('FU',1,5)
                and c.cube_contient_couleur('RU',2,5)
                and c.cube_contient_couleur('BU',3,5)):
                mouvements3 = ('B','B','U','R','Li','B','B','Ri','L','U','B','B')
                c.mouvements(mouvements3)
        else:
            mouvements3 = ('F','F','U','L','Ri','F','F','Li','R','U','F','F')
            c.mouvements(mouvements3)
        return pll(c)

    return c, mouvements1 + mouvements2 + mouvements3

def pll_valide(c):
    if (c.get_facette('FRU',0)==1 and c.get_facette('FRU',1)==2 and c.get_facette('FRU',2)==5):
        if (c.get_facette('LFU',0)==4 and c.get_facette('LFU',1)==1 and c.get_facette('LFU',2)==5):
            if (c.get_facette('RBU',0)==2 and c.get_facette('RBU',1)==3 and c.get_facette('RBU',2)==5):
                if (c.get_facette('BLU',0)==3 and c.get_facette('BLU',1)==4 and c.get_facette('BLU',2)==5):
                    if (c.get_facette('BU',0)==3 and c.get_facette('BU',1)==5):
                        if (c.get_facette('RU',0)==2 and c.get_facette('RU',1)==5):
                            if (c.get_facette('FU',0)==1 and c.get_facette('FU',1)==5):
                                if (c.get_facette('LU',0)==4 and c.get_facette('LU',1)==5):
                                    return True
    return False

if __name__ == '__main__':

    '''
    print("Test avec lecture d'entrée")
    b,c = lecture_cube('WGWBGGYRBOOBRBYOWGRRBOYYORBWWYROGORRYYGOOWBBYGGWWBWGYR')
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
    '''

    tests = tableaux_test()# Fichier test
    i = 0
    for test in tests:
        i += 1
        c = Cube()
        c.scramble(test)
        c,mouv = cross_facile(c)
        validiteCroix = "croix valide" if croix_valide(c) else "CROIX INVALIDE"
        c,mouv2 = ftl(c)
        validiteFtl = "ftl valide" if ftl_valide(c) else "FTL INVALIDE"
        c,mouv3=oll(c)
        validiteOll = "oll valide" if c.face_resolu('U') else "OLL INVALIDE"
        print ("Test "+str(i)+" : "+validiteCroix+" "+validiteFtl+" "+validiteOll+" "+str(len(mouv+mouv2+mouv3)))

