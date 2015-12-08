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
from utils import croix_valide
from test import tableaux_test


def algo_cfop(c):
    '''
    algo

    Prend le cube en entrée, et avec l'algo de résolution choisi, va déterminer la suite de mouvements
    qu'il faut réaliser pour résoudre le cube

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

    if c.get_facette('LD', 0) != 4 : #Si pas bien paramétré, il y a une suite de mouvements à effectuer
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

    if c.get_facette('BD', 0) != 3 : #Si pas bien paramétré, il y a une suite de mouvements à effectuer
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

    if c.get_facette('RD', 0) != 2 : #Si pas bien paramétré, il y a une suite de mouvements à effectuer
        mvtsFix = ('Ri', 'D', 'Bi', 'Di')
        c.mouvements(mvtsFix)
        mouvements4 += mvtsFix

    return c, mouvements1 + mouvements2 + mouvements3 + mouvements4


def ftl(c, mouvements):
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


    # Cube Bleu Orange Blanche
    if c.cube_contient_couleur('LFD',0,1,4):
        pass
    elif c.cube_contient_couleur('FRD',0,1,4):
        c.rot_R()
        c.rot_Li()
        c.rot_U()
        c.rot_L()
        c.rot_Ri()
    elif c.cube_contient_couleur('FRU',0,1,4):
         c.rot_Li()
         c.rot_U()
         c.rot_L()
    elif c.cube_contient_couleur('RBU',0,1,4):
        c.rot_U()
        c.rot_Li()
        c.rot_U()
        c.rot_L()
    elif c.cube_contient_couleur('RBD',0,1,4):
        c.rot_Ri()
        c.rot_U()
        c.rot_Li()
        c.rot_U()
        c.rot_L()
        c.rot_R()
    elif c.cube_contient_couleur('BLD',0,1,4):
        c.rot_L()
        c.rot_U()
        c.rot_U()
        c.rot_L()
        c.rot_L()
        c.rot_U()
        c.rot_L()
    elif c.cube_contient_couleur('BLU',0,1,4):
        c.rot_U()
        c.rot_U()
        c.rot_Li()
        c.rot_U()
        c.rot_L()
    elif c.cube_contient_couleur('LFU',0,1,4):
        c.rot_Ui()
        c.rot_Li()
        c.rot_U()
        c.rot_L()

      # Pas de le bon sens
    while c.get_facette('LFD',2)!=0:
        c.rot_Li()
        c.rot_U()
        c.rot_L()
        c.rot_Ui()
        c.rot_Li()
        c.rot_U()
        c.rot_L()


      # Cube Bleu Rouge Blanche
    if c.cube_contient_couleur('FRD',0,1,2):
        pass
    elif c.cube_contient_couleur('FRU',0,1,2):
        c.rot_U()
        c.rot_R()
        c.rot_Ui()
        c.rot_Ri()
    elif c.cube_contient_couleur('LFU',0,1,2):
        c.rot_R()
        c.rot_Ui()
        c.rot_Ri()
    elif c.cube_contient_couleur('RBU',0,1,2):
        c.rot_U()
        c.rot_U()
        c.rot_R()
        c.rot_Ui()
        c.rot_Ri()
    elif c.cube_contient_couleur('RBD',0,1,2):
        c.rot_Ri()
        c.rot_U()
        c.rot_U()
        c.rot_R()
        c.rot_R()
        c.rot_Ui()
        c.rot_Ri()
    elif c.cube_contient_couleur('BLD',0,1,2):
        c.rot_L()
        c.rot_Ui()
        c.rot_Li()
        c.rot_Ui()
        c.rot_R()
        c.rot_Ui()
        c.rot_Ri()
    elif c.cube_contient_couleur('BLU',0,1,2):
        c.rot_Ui()
        c.rot_R()
        c.rot_Ui()
        c.rot_Ri()

    while c.get_facette('FRD',2)!=0:
        c.rot_R()
        c.rot_Ui()
        c.rot_Ri()
        c.rot_U()
        c.rot_R()
        c.rot_Ui()
        c.rot_Ri()

    if c.cube_contient_couleur('BLD',0,3,4):
        pass
    elif c.cube_contient_couleur('FRU',0,3,4):
        c.rot_Ui()
        c.rot_L()
        c.rot_Ui()
        c.rot_Li()
    elif c.cube_contient_couleur('RBU',0,3,4):
        c.rot_L()
        c.rot_Ui()
        c.rot_Li()
    elif c.cube_contient_couleur('RBD',0,3,4):
        c.rot_Ri()
        c.rot_L()
        c.rot_Ui()
        c.rot_Li()
        c.rot_R()
    elif c.cube_contient_couleur('BLU',0,3,4):
        c.rot_U()
        c.rot_L()
        c.rot_Ui()
        c.rot_Li()
    elif c.cube_contient_couleur('LFU',0,3,4):
        c.rot_U()
        c.rot_U()
        c.rot_L()
        c.rot_Ui()
        c.rot_Li()

    while c.get_facette('BLD',2)!=0:
        c.rot_L()
        c.rot_Ui()
        c.rot_Li()
        c.rot_U()
        c.rot_L()
        c.rot_Ui()
        c.rot_Li()

    if c.cube_contient_couleur('RBD',0,2,3):
        pass
    elif c.cube_contient_couleur('FRU',0,2,3):
        c.rot_U()
        c.rot_U()
        c.rot_Ri()
        c.rot_U()
        c.rot_R()
    elif c.cube_contient_couleur('RBU',0,2,3):
        c.rot_Ui()
        c.rot_Ri()
        c.rot_U()
        c.rot_R()
    elif c.cube_contient_couleur('BLU',0,2,3):
        c.rot_Ri()
        c.rot_U()
        c.rot_R()
    elif c.cube_contient_couleur('LFU',0,2,3):
        c.rot_U()
        c.rot_Ri()
        c.rot_U()
        c.rot_R()

    while c.get_facette('RBD',2)!=0:
        c.rot_Ri()
        c.rot_U()
        c.rot_R()
        c.rot_Ui()
        c.rot_Ri()
        c.rot_U()
        c.rot_R()

    #####################
    # Deuxième couronne #
    #####################

    # Vert Rouge 
    if c.cube_contient_couleur('FR',3,2):
      pass
    elif c.cube_contient_couleur('FU',3,2):
        c.rot_B()
        c.rot_Ui()
        c.rot_Bi()
        c.rot_Ui()
        c.rot_Ri()
        c.rot_U()
        c.rot_R()
   # elif c.cube_contient_couleur('FL',3,2):

    elif c.cube_contient_couleur('RU',3,2):
        c.rot_U()
        c.rot_B()
        c.rot_Ui()
        c.rot_Bi()
        c.rot_Ui()
        c.rot_Ri()
        c.rot_U()
        c.rot_R()
    elif c.cube_contient_couleur('LU',3,2):
        c.rot_Ui()
        c.rot_B()
        c.rot_Ui()
        c.rot_Bi()
        c.rot_Ui()
        c.rot_Ri()
        c.rot_U()
        c.rot_R()
    #elif c.cube_contient_couleur('BR',3,2):
   # elif c.cube_contient_couleur('BL',3,2):
    elif c.cube_contient_couleur('BU',3,2):
        c.rot_U()
        c.rot_U()
        c.rot_B()
        c.rot_Ui()
        c.rot_Bi()
        c.rot_Ui()
        c.rot_Ri()
        c.rot_U()
        c.rot_R()

    # Face Orange Vert
    if c.cube_contient_couleur('FU',3,4):
        if c.get_facette('FU',0)==3:
            c.rot_Ui()
            c.rot_L()
            c.rot_Ui()
            c.rot_Li()
            c.rot_Ui()
            c.rot_Bi()
            c.rot_U()
            c.rot_B()
        elif c.get_facette('FU',0)==4:
            c.rot_Bi()
            c.rot_U()
            c.rot_B()
            c.rot_U()
            c.rot_L()
            c.rot_Ui()
            c.rot_Li()
    elif c.cube_contient_couleur('RU',3,4):
        if c.get_facette('RU',0)==3:
            c.rot_L()
            c.rot_Ui()
            c.rot_Li()
            c.rot_Ui()
            c.rot_Bi()
            c.rot_U()
            c.rot_B()
        elif c.get_facette('RU',0)==4:
            c.rot_U()
            c.rot_Bi()
            c.rot_U()
            c.rot_B()
            c.rot_U()
            c.rot_L()
            c.rot_Ui()
            c.rot_Li()
    elif c.cube_contient_couleur('LU',3,4):
        if c.get_facette('LU',0)==3:
            c.rot_U()
            c.rot_U()
            c.rot_L()
            c.rot_Ui()
            c.rot_Li()
            c.rot_Ui()
            c.rot_Bi()
            c.rot_U()
            c.rot_B()
        elif c.get_facette('LU',0)==4:
            c.rot_Ui()
            c.rot_Bi()
            c.rot_U()
            c.rot_B()
            c.rot_U()
            c.rot_L()
            c.rot_Ui()
            c.rot_Li()
    elif c.cube_contient_couleur('BU',3,4):
        if c.get_facette('BU',0)==3:
            c.rot_U()
            c.rot_L()
            c.rot_Ui()
            c.rot_Li()
            c.rot_Ui()
            c.rot_Bi()
            c.rot_U()
            c.rot_B()
        elif c.get_facette('BU',0)==4:
            c.rot_U()
            c.rot_U()
            c.rot_Bi()
            c.rot_U()
            c.rot_B()
            c.rot_U()
            c.rot_L()
            c.rot_Ui()
            c.rot_Li()

    # Bleu Orange
    if c.cube_contient_couleur('FU',1,4):
        if c.get_facette('FU',0)==4:
            c.rot_U()
            c.rot_U()
            c.rot_F()
            c.rot_Ui()
            c.rot_Fi()
            c.rot_Ui()
            c.rot_Li()
            c.rot_U()
            c.rot_L()
        elif c.get_facette('FU',0)==1:
            c.rot_Ui()
            c.rot_Li()
            c.rot_U()
            c.rot_L()
            c.rot_U()
            c.rot_F()
            c.rot_Ui()
            c.rot_Fi()
    elif c.cube_contient_couleur('RU',1,4):
        c.rot_Ui()
        c.rot_F()
        c.rot_Ui()
        c.rot_Fi()
        c.rot_Ui()
        c.rot_Li()
        c.rot_U()
        c.rot_L()
    elif c.cube_contient_couleur('LU',1,4):
        c.rot_U()
        c.rot_F()
        c.rot_Ui()
        c.rot_Fi()
        c.rot_Ui()
        c.rot_Li()
        c.rot_U()
        c.rot_L()
    elif c.cube_contient_couleur('BU',1,4):
        c.rot_F()
        c.rot_Ui()
        c.rot_Fi()
        c.rot_Ui()
        c.rot_Li()
        c.rot_U()
        c.rot_L()

    # Rouge bleu
    if c.cube_contient_couleur('FU',1,2):
        c.rot_U()
        c.rot_R()
        c.rot_Ui()
        c.rot_Ri()
        c.rot_Ui()
        c.rot_Fi()
        c.rot_U()
        c.rot_F()
    elif c.cube_contient_couleur('RU',1,2):
        c.rot_U()
        c.rot_U()
        c.rot_R()
        c.rot_Ui()
        c.rot_Ri()
        c.rot_Ui()
        c.rot_Fi()
        c.rot_U()
        c.rot_F()
    elif c.cube_contient_couleur('LU',1,2):
        c.rot_R()
        c.rot_Ui()
        c.rot_Ri()
        c.rot_Ui()
        c.rot_Fi()
        c.rot_U()
        c.rot_F()
    elif c.cube_contient_couleur('BU',1,2):
        c.rot_Ui()
        c.rot_R()
        c.rot_Ui()
        c.rot_Ri()
        c.rot_Ui()
        c.rot_Fi()
        c.rot_U()
        c.rot_F()


    # Traiter le cas ou le cube n'est pas dans le bon sens 
    # Et lorsque le cube est sur un coté

    return c

def ftl_valide(c):
    if (c.get_facette('RBD',2) and c.get_facette('BLD',2) and c.get_facette('FRD',2) and c.get_facette('LFD',2))==0: #face blanche
        if c.get_facette('RBD',1)==3 and c.get_facette('RBD',0)==2:
            if c.get_facette('BLD',1)==4 and c.get_facette('BLD',0)==3:
                if c.get_facette('FRD',1)==2 and c.get_facette('FRD',0)==1:
                    if c.get_facette('LFD',1)==1 and c.get_facette('LFD',0)==4:
                        return True
    return False

def oll(c, mouvements):
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
    #Test si déjà croix jaune

    #Test si une seule pièce jaune en bas 
    #Test toutes les possibilités 

#def pll(c, mouvements):
'''
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
        c {Cube}, mouvements {String} l'objet cube, à résoudre

    :Returns:x
        {Cube|Boolean}, {String|None} L'objet cube avec la face jaune de faite, ou False si cube pas resolvable
                         Liste des mouvements à faire, ou rien si cube pas resolvable
    '''

if __name__ == '__main__':


  # ---------------- test CROIX
  print("Test avec lecture d'entrée")

  b,c = lecture_cube('OGRBWYBGBGYYOYOWOWGRYOOOBGBRRYRBWWWRBWYGROWGRYBRGYWBOG')
  print(c)
  print()
  print("CROSS")
  c,mouv = cross_facile(c)
  print(c)
  print('Mouvements à effectuer :', mouv)
  print("FIRST TWO LAYERS")
  c = ftl(c,[])
  print(c)
  print()
  c2 = c
  print("Test avec mouvements")

  #Test OLL   
  print("Test OLL avant")
  print(c)
  c=oll(c,[])
  print("Test OLL")
  print(c)

  tests = tableaux_test()# Fichier test

  i = 0
  for test in tests:
    i += 1
    c = Cube()
    c.mouvements(test)
    c,mouv = cross_facile(c)
    validiteCroix = "croix valide" if croix_valide(c) else "CROIX INVALIDE"
    c = ftl(c,[])
    validiteFtl = "ftl valide" if ftl_valide(c) else "FTL INVALIDE"
    print ("Test "+str(i)+" : "+validiteCroix+" "+validiteFtl)
    #print(c)



#-------------------------FIN TEST CROIX
