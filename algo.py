from Cube import Cube
from lire_entree import lecture_cube
from test import tableaux_test
'''
Algo de résolution 


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


'''




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

#Etape 1 de l'algo
# résumé de la vidéo pour obtenir une croix
'''
cette vidéo est une vidéo pour les débutants.
Une fois celle là bien maîtrisée, aller voir celle là pour optimiser
" THE ADVANCED CROSS"
https://www.youtube.com/watch?feature=player_detailpage&v=WzE7SyDB8vA
-On repère le côté où le centre est blanc
-On la met au top
-On fait un centre blanc et une face adjacente blanche aussi
-Sur la Face qui a l'arête en commun on 
... 

-forum
http://forum.francocube.com/viewtopic.php?t=5464
Il précise sur ce forum que pour réaliser une croix , c'est 8 mouvements maximum, et 7 dans la majorité des cas

scrambler de rubiks :
http://ruwix.com/puzzle-scramble-generator/

'''
def cross_facile(c, mouvements):
    '''
    Etape 1 de l'algo CFOP
    Prend le cube en entrée et réalise la première étape de l'algo CFOP
    c'est à dire réalisé une croix sur la face blanche et en plus avoir 
    2 couleurs identiques à chaque extremités de la croix, exemple : 
           X W X
           W W W
           X W X
    X O X  X G X  X R X  X B X
    X O X  X G X  X R X  X B X
    X X X  X X X  X X X  X X X
           X X X
           X X X
           X X X

    :Args:
        c {Cube}, mouvements {String} l'objet cube, à résoudre
                                      Liste des mouvements à réalisé qui sera complété au fur 
                                      et à mesure des étapes de l'algo

    :Returns:
        {Cube}, {String} L'objet cube avec la croix blanche faite 
                         Liste des mouvements à faire
    '''


    #On veut mettre l'arrête bleue blanche sur à côté de la pièce centrale blanc  
    #le placer en FB jsute en dessous la pièce centrale bleue
    #On cherche l'arête bleue blanche
    #Si elle est sur la première couronne
    if c.cube_contient_couleur('FU',0,1):
      c.rot_F()
      c.rot_F()
    elif c.cube_contient_couleur('RU',0,1):
      c.rot_U()
      c.rot_F()
      c.rot_F()
    elif c.cube_contient_couleur('BU',0,1):
      c.rot_U()
      c.rot_U()
      c.rot_F()
      c.rot_F()
    elif c.cube_contient_couleur('LU',0,1):
      c.rot_Ui()
      c.rot_F()
      c.rot_F()
    #Deuxième couronne
    elif c.cube_contient_couleur('FR',0,1):
      c.rot_R()
      c.rot_U()
      c.rot_F()
      c.rot_F()
    elif c.cube_contient_couleur('BR',0,1):
      c.rot_Ri()
      c.rot_U()
      c.rot_F()
      c.rot_F()    
    elif c.cube_contient_couleur('BL',0,1):
      c.rot_Bi()
      c.rot_U()
      c.rot_U()
      c.rot_F()
      c.rot_F()  
    elif c.cube_contient_couleur('FL',0,1):
      c.rot_Fi()
    #Troisième couronne, autour du blanc
    elif c.cube_contient_couleur('LD',0,1):
      c.rot_L()
      c.rot_L()
      c.rot_Ui()
      c.rot_F()
      c.rot_F()
    elif c.cube_contient_couleur('RD',0,1):
      c.rot_R()
      c.rot_R()
      c.rot_U()
      c.rot_F()
      c.rot_F()
    elif c.cube_contient_couleur('BD',0,1):
      c.rot_B()
      c.rot_B()
      c.rot_U()
      c.rot_U()
      c.rot_F()
      c.rot_F()
    #A ce niveau là , l'arrête bleue blanche est au niveau de la troisième couronne
    # à l'endroit où il faut mais pas forcément paramétré comme il le faut : WWBB et pas WBWB
    if c.get_facette('FD',0) != 1 : #Si pas bien paramétré, il y a une suite de mouvements à effectuer
      c.rot_Fi()
      c.rot_B()
      c.rot_Ri()
      c.rot_Di()
    
    #LA PARTIE BLANC BLEUE EST COMPLETEE
    '''print('blanc bleu')
    print(c)
    print()'''
    
    # On fait pareil pour la partie orange
    #Si elle est sur la première couronne
    if c.cube_contient_couleur('FU',0,4):
      c.rot_U()
      c.rot_L()
      c.rot_L()
    elif c.cube_contient_couleur('RU',0,4):
      c.rot_U()
      c.rot_U()
      c.rot_L()
      c.rot_L()
    elif c.cube_contient_couleur('BU',0,4):
      c.rot_Ui()
      c.rot_L()
      c.rot_L()
    elif c.cube_contient_couleur('LU',0,4):
      c.rot_L()
      c.rot_L()
    #Deuxième couronne
    elif c.cube_contient_couleur('FR',0,4):
      c.rot_R()
      c.rot_U()
      c.rot_U()
      c.rot_L()
      c.rot_L()
    elif c.cube_contient_couleur('BR',0,4):
      c.rot_B()
      c.rot_Ui()
      c.rot_L()
      c.rot_L()    
    elif c.cube_contient_couleur('BL',0,4):
      c.rot_Li()
    elif c.cube_contient_couleur('FL',0,4):
      c.rot_L()
    #Troisième couronne, autour du blanc
    elif c.cube_contient_couleur('RD',0,4):
      c.rot_R()
      c.rot_R()
      c.rot_U()
      c.rot_U()
      c.rot_L()
      c.rot_L()
    elif c.cube_contient_couleur('BD',0,4):
      c.rot_B()
      c.rot_B()
      c.rot_Ui()
      c.rot_L()
      c.rot_L()
    #A ce niveau là , l'arrête orange blanche est au niveau de la troisième couronne

    # à l'endroit où il faut mais pas forcément paramétré comme il le faut : WWOO et pas WOWO
    if c.get_facette('LD',0) != 4 : #Si pas bien paramétré, il y a une suite de mouvements à effectuer
      c.rot_Li()
      c.rot_D()
      c.rot_Fi()
      c.rot_Di()
      
    '''print('blanc orange')
    print(c)
    print()'''
    



    #PAREIL POUR VERT
 #Si elle est sur la première couronne

    if c.cube_contient_couleur('FU',0,3):      
      c.rot_U()
      c.rot_U()
      c.rot_B()
      c.rot_B()
    elif c.cube_contient_couleur('RU',0,3):      
      c.rot_Ui()
      c.rot_B()
      c.rot_B()
    elif c.cube_contient_couleur('BU',0,3): 
      c.rot_B()
      c.rot_B()
    elif c.cube_contient_couleur('LU',0,3):
      c.rot_U()
      c.rot_B()
      c.rot_B()
    #Deuxième couronne
    elif c.cube_contient_couleur('FR',0,3):
      c.rot_R()
      c.rot_Ui()
      c.rot_B()
      c.rot_B()
    elif c.cube_contient_couleur('BL',0,3):
      c.rot_B()    
    elif c.cube_contient_couleur('BR',0,3): #PROBLEME ICI, VEUT PAS RENTRER DANS LA CONDITION POUR LE TEST 4
      c.rot_Bi()    
    elif c.cube_contient_couleur('FL',0,3):
      c.rot_Li()
      c.rot_U()
      c.rot_L() # Pour remettre la partie d'avant à sa place
      c.rot_B()
      c.rot_B()
    #Troisième couronne, autour du blanc
    elif c.cube_contient_couleur('RD',0,3):
      c.rot_R()
      c.rot_R()
      c.rot_Ui()
      c.rot_B()
      c.rot_B()
    #A ce niveau là , l'arrête orange blanche est au niveau de la troisième couronne

    # à l'endroit où il faut mais pas forcément paramétré comme il le faut : WWGG et pas WGWG
    if c.get_facette('BD',0) != 3 : #Si pas bien paramétré, il y a une suite de mouvements à effectuer
      c.rot_Bi()
      c.rot_D()
      c.rot_Li()
      c.rot_Di()

      #Partie verte finie
    '''print('blanc vert')
    print(c)
    print()'''

      #Dernière partie de la croix : la partie rouge
 #Si elle est sur la première couronne

    if c.cube_contient_couleur('FU',0,2):
      c.rot_Ui()
      c.rot_R()
      c.rot_R()
    elif c.cube_contient_couleur('RU',0,2):
      c.rot_R()
      c.rot_R()
    elif c.cube_contient_couleur('BU',0,2):
      c.rot_U()
      c.rot_R()
      c.rot_R()    
    elif c.cube_contient_couleur('LU',0,2):
      c.rot_U()
      c.rot_U()
      c.rot_R()
      c.rot_R()
    #Deuxième couronne
    elif c.cube_contient_couleur('FR',0,2):
      c.rot_Ri()
    elif c.cube_contient_couleur('BL',0,2):
      c.rot_Bi()
      c.rot_U()
      c.rot_B()#Pour remettre à sa place les éléments déplacés dans Bi
      c.rot_R()
      c.rot_R()
    elif c.cube_contient_couleur('BR',0,2):
      c.rot_R()    
    elif c.cube_contient_couleur('FL',0,2):
      c.rot_F()
      c.rot_Ui()
      c.rot_Fi()
      c.rot_R()
      c.rot_R()

    '''print('blanc rouge')
    print(c)
    print()'''
    #A ce niveau là , l'arrête rouge blanche est au niveau de la troisième couronne

    # à l'endroit où il faut mais pas forcément paramétré comme il le faut : WWRR et pas WOWR
    if c.get_facette('RD',0) != 2 : #Si pas bien paramétré, il y a une suite de mouvements à effectuer
      c.rot_Ri()
      c.rot_D()
      c.rot_Bi()
      c.rot_Di()

    return c,mouvements    

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

  b,c = lecture_cube('YWROYGOGWGGYGYOGRWGBRGOOWBBORYOGWOBBYWRWRWOYBRRBRWYYBB')
  print(c)
  print()
  print("CROSS")
  c,mouv = cross_facile(c,[])
  print(c)
  print("FIRST TWO LAYERS")
  c = ftl(c,[])
  print(c)
  
  '''print("Test avec mouvements")

  tests = tableaux_test()# Fichier test

  i = 0
  for test in tests:
    i += 1
    c = Cube()
    c.scramble(test)
    c,mouv = cross_facile(c,[])
    validite = "croix valide" if croix_valide(c) else "CROIX INVALIDE"
    print ("Test"+str(i)+" : "+validite)
    #print(c)
    '''
  #Si une croix est invalide, on regarde son cas spécifiquement dans les tests
  '''c = Cube()
  c.scramble(tests[23])
  c,mouv = cross_facile(c,[])
  print ("Test 24")
  print(c)'''


#-------------------------FIN TEST CROIX