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
https://www.youtube.com/watch?v=IMb7hOAgmng

Utile : mouvementsr de rubiks :
----------------------------
http://ruwix.com/puzzle-mouvements-generator/

'''

from Cube import Cube
from lire_entree import lecture_cube
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

def cross_facile(c, m):
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
        {Cube}, {String}        L'objet cube avec la croix blanche faite
                                Liste des mouvements à faire
    '''

    mouvements = None #liste des mouvements à effectués

    #On veut mettre l'arrête bleue-blanche à côté de la pièce centrale blanche
    #ie. la placer en FB jsute en dessous la pièce centrale bleue

    #On cherche l'arête bleue blanche
    if c.cube_contient_couleur('FU', 0, 1): #Si elle est sur la première couronne
        mouvements = ('F2',)
    elif c.cube_contient_couleur('RU', 0, 1):
        mouvements = ('U', 'F2')
    elif c.cube_contient_couleur('BU', 0, 1):
        mouvements = ('U2', 'F2')
    elif c.cube_contient_couleur('LU', 0, 1):
        mouvements = ('Ui', 'F2')

    elif c.cube_contient_couleur('FR', 0, 1): #Deuxième couronne
        mouvements = ('R', 'U', 'F2')
    elif c.cube_contient_couleur('BR', 0, 1):
        mouvements = ('Ri', 'U', 'F2')
    elif c.cube_contient_couleur('BL', 0, 1):
        mouvements = ('Bi', 'U2', 'F2')
    elif c.cube_contient_couleur('FL', 0, 1):
        mouvements = ('Fi',)

    elif c.cube_contient_couleur('LD', 0, 1): #Troisième couronne, autour du blanc
        mouvements = ('L2', 'Ui', 'F2')
    elif c.cube_contient_couleur('RD', 0, 1):
        mouvements = ('R2', 'U', 'F2')
    elif c.cube_contient_couleur('BD', 0, 1):
        mouvements = ('B2', 'U2', 'F2')

    if mouvements:
        c.mouvements(mouvements) #on effectue les mouvements

    mouvements = None

    #À ce niveau là, l'arrête bleue-blanche est au niveau de la troisième couronne
    #à l'endroit où il faut mais pas forcément paramétré comme il le faut: WWBB et pas WBWB

    if c.get_facette('FD', 0) != 1 : #Si pas bien paramétré,
                                     #il y a une suite de mouvements à effectuer
        c.mouvements(('Fi', 'B', 'Ri', 'Di'))

    #La partie blanc-bleue est complétée

    #On fait pareil pour la partie orange

    if c.cube_contient_couleur('FU', 0, 4): #Si elle est sur la première couronne
        mouvements = ('U', 'L2')
    elif c.cube_contient_couleur('RU', 0, 4):
        mouvements = ('U2', 'L2')
    elif c.cube_contient_couleur('BU', 0, 4):
        mouvements = ('Ui', 'L2')
    elif c.cube_contient_couleur('LU', 0, 4):
        mouvements = ('L2',)

    elif c.cube_contient_couleur('FR', 0, 4): #Deuxième couronne
        mouvements = ('R', 'U2', 'L2')
    elif c.cube_contient_couleur('BR', 0, 4):
        mouvements = ('B', 'Ui', 'L2')
    elif c.cube_contient_couleur('BL', 0, 4):
        mouvements = ('Li',)
    elif c.cube_contient_couleur('FL', 0, 4):
        mouvements = ('L',)

    elif c.cube_contient_couleur('RD', 0, 4): #Troisième couronne, autour du blanc
        mouvements = ('R2', 'U2', 'L2')
    elif c.cube_contient_couleur('BD', 0, 4):
        mouvements = ('B2', 'Ui', 'L2')

    if mouvements:
        c.mouvements(mouvements) #on effectue les mouvements

    mouvements = None

    #A ce niveau là, l'arrête orange blanche est au niveau de la troisième couronne
    #à l'endroit où il faut mais pas forcément paramétré comme il le faut : WWOO et pas WOWO

    if c.get_facette('LD', 0) != 4 : #Si pas bien paramétré, il y a une suite de mouvements à effectuer
        c.mouvements(('Li', 'D', 'Fi', 'Di'))

    #La partie orange est complétée

    #On fait pareil pour la partie verte

    if c.cube_contient_couleur('FU', 0 ,3): #Si elle est sur la première couronne
        mouvements = ('U2', 'B2')
    elif c.cube_contient_couleur('RU', 0 ,3):
        mouvements = ('Ui', 'B2')
    elif c.cube_contient_couleur('BU', 0 ,3):
        mouvements = ('B2',)
    elif c.cube_contient_couleur('LU', 0 ,3):
        mouvements = ('U', 'B2')

    elif c.cube_contient_couleur('FR', 0 ,3): #Deuxième couronne
        mouvements = ('R', 'Ui', 'B2')
    elif c.cube_contient_couleur('BL', 0 ,3):
        mouvements = ('B',)
    elif c.cube_contient_couleur('BR', 0 ,3):
        mouvements = ('Bi',)
    elif c.cube_contient_couleur('FL', 0 ,3):
        mouvements = (
            'Li', 'U',
            'L', # Pour remettre la partie d'avant à sa place
            'B2'
        )

    elif c.cube_contient_couleur('RD', 0 ,3): #Troisième couronne, autour du blanc
        mouvements = ('R2', 'Ui', 'B2')

    if mouvements:
        c.mouvements(mouvements) #on effectue les mouvements

    mouvements = None

    #À ce niveau là, l'arrête verte blanche est au niveau de la troisième couronne
    #à l'endroit où il faut mais pas forcément paramétré comme il le faut : WWGG et pas WGWG

    if c.get_facette('BD', 0) != 3 : #Si pas bien paramétré, il y a une suite de mouvements à effectuer
        c.mouvements(('Bi', 'D', 'Li', 'Di'))

    #La partie verte est complétée

    #On fait pareil pour la partie rouge

    if c.cube_contient_couleur('FU', 0 ,2): #Si elle est sur la première couronne
        mouvements = ('Ui', 'R2')
    elif c.cube_contient_couleur('RU', 0 ,2):
        mouvements = ('R2',)
    elif c.cube_contient_couleur('BU', 0 ,2):
        mouvements = ('U', 'R2')
    elif c.cube_contient_couleur('LU', 0 ,2):
        mouvements = ('U2', 'R2')

    elif c.cube_contient_couleur('FR', 0 ,2): #Deuxième couronne
        mouvements = ('Ri',)
    elif c.cube_contient_couleur('BL', 0 ,2):
        mouvements = (
            'Bi', 'U',
            'B', # Pour remettre la partie d'avant à sa place
            'R2'
        )

    elif c.cube_contient_couleur('BR', 0 ,2):
        mouvements = ('R',)
    elif c.cube_contient_couleur('FL', 0 ,2):
        mouvements = ('F', 'Ui', 'Fi', 'R2')

    if mouvements:
        c.mouvements(mouvements) #on effectue les mouvements

    mouvements = None

    #A ce niveau là, l'arrête rouge blanche est au niveau de la troisième couronne
    #à l'endroit où il faut mais pas forcément paramétré comme il le faut : WWRR et pas WOWR

    if c.get_facette('RD', 0) != 2 : #Si pas bien paramétré, il y a une suite de mouvements à effectuer
        c.mouvements(('Ri', 'D', 'Bi', 'Di'))

    return c, m

def croix_valide(c):
  bool = False
  if (c.get_facette('FD',1) and c.get_facette('RD',1) and c.get_facette('BD',1) and c.get_facette('LD',1)) == 0: # croix blanche
    if (c.get_facette('FD',0) == 1 and c.get_facette('RD',0) == 2 and c.get_facette('BD',0) == 3 and c.get_facette('LD',0) == 4):
      bool = True
  return bool


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

    return c

def ftl_valide(c):
    if (c.get_facette('RBD',2) and c.get_facette('BLD',2) and c.get_facette('FRD',2) and c.get_facette('LFD',2))==0: #face blanche
        if c.get_facette('RBD',1)==3 and c.get_facette('RBD',0)==2:
            if c.get_facette('BLD',1)==4 and c.get_facette('BLD',0)==3:
                if c.get_facette('FRD',1)==2 and c.get_facette('FRD',0)==1:
                    if c.get_facette('LFD',1)==1 and c.get_facette('LFD',0)==4:
                        return True
    return False

#def oll(c, mouvements):
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
  c,mouv = cross_facile(c,[])
  print(c)
  print("FIRST TWO LAYERS")
  c = ftl(c,[])
  print(c)
  print()

  print("Test avec mouvements")

  tests = tableaux_test()# Fichier test

  i = 0
  for test in tests:
    i += 1
    c = Cube()
    c.mouvements(test)
    c,mouv = cross_facile(c,[])
    validiteCroix = "croix valide" if croix_valide(c) else "CROIX INVALIDE"
    c = ftl(c,[])
    validiteFtl = "ftl valide" if ftl_valide(c) else "FTL INVALIDE"
    print ("Test "+str(i)+" : "+validiteCroix+" "+validiteFtl)
    #print(c)

  #Si une croix est invalide, on regarde son cas spécifiquement dans les tests
  '''c = Cube()
  c.mouvements(tests[23])
  c,mouv = cross_facile(c,[])
  print ("Test 24")
  print(c)'''


#-------------------------FIN TEST CROIX
