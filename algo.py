from Cube import Cube
from lire_entree import lecture_cube
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


#def ftl(c, mouvements):
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
  '''print("Test avec lecture d'entrée")

  b,c = lecture_cube('YWROYGOGWGGYGYOGRWGBRGOOWBBORYOGWOBBYWRWRWOYBRRBRWYYBB')
  print(c)
  print()
  c,mouv = cross_facile(c,[])
  print(c)
  print()'''
  
tests = [
  "D B2 D' B2 U2 R2 F2 R2 B2 R2 U F' L B U2 L2 R B U B F'",
  "B' D2 B' L2 B' R2 U2 L2 F L2 U F2 L F2 D2 B U L2 F' R",
  "L2 F' U2 F2 D2 U2 F' R2 F U' B U2 B R2 F2 L B' R F",
  "U F' L2 B2 L F' D' F2 U2 F U' F2 U F2 U F2 D2 L2 B2", 
  "B2 U' R L2 B L' F2 D L2 D R' B L2 U2 D2 F' D2 F' D2 R2",
  "D B2 D' B2 U2 R2 F2 R2 B2 R2 U F' L B U2 L2 R B U B F'",
  "B' D2 B' L2 B' R2 U2 L2 F L2 U F2 L F2 D2 B U L2 F' R",
  "U F' L2 B2 L F' D' F2 U2 F U' F2 U F2 U F2 D2 L2 B2", 
  "L2 F' U2 F2 D2 U2 F' R2 F U' B U2 B R2 F2 L B' R F",
  "B2 U' R L2 B L' F2 D L2 D R' B L2 U2 D2 F' D2 F' D2 R2",
  "D2 B L2 D2 L U' R D2 B D L2 B2 R' F2 R' D2 L F2 L2",
  "B2 L2 D B2 D F2 U' B2 U L2 D' F' R D2 L' B' U' L F R2",
  "D2 L2 U2 B F D2 F U2 F2 D F R' U R2 U' F' L' R2 F' R",
  "L2 D2 F2 R U2 R2 D2 U2 F2 R' F2 U' B D2 L F2 U B R2 B'",
  "B' F' U2 B D2 F' L2 D2 U' R B2 F' L D' R2 F' L U B",
  "B R2 D2 U2 B2 L2 F' U2 R2 U R B' F2 U' B' U L2 F' U",
  "U2 B2 L2 B F2 L2 U2 R' D2 B2 R F' L R' B' F2 R",
  "B2 R2 B2 L U2 L2 B2 D2 B' L2 B F2 L' U B2 U2 L D' B",
  "L B' U2 B' L' D R' D2 R2 U' F R2 F2 U B2 D2 F2 L2 F2 D'", 
  "L2 U' R' B' U2 R' D2 B' D' L2 B' L2 F' U2 F2 B2 L2 U2 R2 D2",
  "U2 B2 F2 U F2 U2 R2 F D R' U L R D2 L' D' R' B F",
  "D R' B U2 R' B' U B U' D' B' L' U2 L2 D2 L' F2 L' U2",
  "U2 F2 U' F2 U B2 F2 D' L' U' F2 D2 L2 U2 F' D L F' R2 F",
  "D2 F R F B L2 D R' D2 F D F2 R2 F2 U2 B2 R2 D2 R'", 
  "R' B2 D2 B2 R' D2 R' B2 L2 F' U' L' F L2 U2 F D R2 U B2",
  "D2 F2 D L2 R2 B2 U R2 F2 R2 U2 L D' U' L R' B' L B2 D' U'",
  "U2 R' F U B R2 U B' L' U2 B2 U B2 U B2 L2 B2 D' F2",
  "F2 R F2 L D2 F2 D2 F2 D L R' U2 B2 F' R' U L B",
  "D F R2 D' B2 U2 D2 L B D2 F U2 D L2 U2 B2 L2 B2",
  "F2 U2 R2 L' B D' L2 U' F' R L U' D2 L2 F2 B2 D2 F2 R2",
  "B2 L B2 L' D2 L' F2 D L2 B F' R U' F L2 D' F' U",
  "R B' U' B D2 R2 F L2 F2 B' R B2 D L2 B2 U2 B2 U2 R2",
  "U' D2 R U2 B D R L' U2 L' F' R' D2 R' U2 R' B2 R' D2 R",
  "U' D L2 U' D2 F U L' F2 U R' B2 D L2 B2 U R2 U2 R2",
  "R D2 B2 R' F2 D2 R F2 D2 L2 F' U' R U2 B F2 R U R2 D2",
  "R' B' R' L F' U2 R' D2 R' U' F' R2 B R2 B2 D2 L2 D2 F' U2",
  "D2 F2 D L2 U' R2 U2 F2 L2 B' U L D' B F U' L' R2 F2",
  "B2 U2 F2 L2 U2 B D2 U2 B L' F' D L2 B D' B2 F L' R U'",
  "R F2 D F' B' D R U' L U2 D L2 F' L2 U2 B R2 B' D2 B2",
  "D' R2 D' L2 B2 U' L2 D2 L' B D2 L2 F R2 D L2 B R' B",
  "B' R B D F2 R D2 L B2 D' R' D2 R' F2 D2 F2 U2 R' B2 R",
  "B2 L U2 R U2 B2 L' B2 F2 R D B R' U B' L2 F' U' F2 R2",
  "F2 L' B2 F2 D2 B2 R' F2 R2 U2 F2 U' B' L B2 D' R B D F'",
  "F2 R2 D' L' D2 F' L F' U2 B2 D' B2 L B2 L' F2 R",
  "D' B2 L2 R2 U' B2 U2 F' L B2 L U' B U2 F2 L2 U' L' U",
  "R B2 L' R' D2 B2 R2 B2 R' B' D F2 D' R2 B2 F2 R U B2",
  "B2 R2 L2 U D F2 D F L' F2 U2 D2 F2 D' R2 U' F2",
  "B' U R L' D2 L U2 D' B' U L' D2 R B2 R2 U2 D2 L F2",
  "R2 B' L2 B' U2 F L2 D2 U2 B2 R' D' F D' R' B' L' D' U' L2",
  "R2 F2 L2 B' R2 F' U2 B' F' D2 L B2 R' D F R F' L B L'",
  "F2 L2 D' L2 U' R2 D2 F' L2 B' F D2 R B2 U B2 U2 L U",
  "B2 L2 U L2 D R2 U' R2 B2 L' D2 U2 R' U F L2 F2 U' L U2",
  "F2 L2 U2 R' F2 R F2 U2 B2 R' B L2 B' D2 B2 L' D F R2",
  "R2 F2 L2 B2 R2 B D2 R2 B' D' L' D' B F L U2 L B' F2",
  "F' U' D2 F2 L U' D2 R2 D2 R D' L2 B L2 F U2 F' R2 U2",
  "D2 F2 U' R2 D' U2 F2 U2 R U' R2 F2 R B' R2 U' F D'",
  "R L2 U B2 D' F2 B' R2 D' R L2 D F2 R2 L2 U' B2 D2 F2 L2",
  "R2 D B2 D F2 D L2 F R B' F R2 U' F' L R2 D2",
  "B2 L2 D2 L2 F' R2 F2 L U L2 D' U B' L' R2 U B'",
  "B' D2 L2 B2 R2 B R2 U2 B2 U R' D' U L U L2 U2 L' U2 F",
  "L2 U' B2 U B2 D2 L2 U' R U L F L2 D' L R U F",
  "B L2 R2 F2 D2 B' D2 U2 L' R' F D U' R2 D2 F D2 U2" 
]


i = 0
for test in tests:
  i += 1
  c = Cube()
  c.scramble(test)
  c,mouv = cross_facile(c,[])
  validite = "croix valide" if croix_valide(c) else "CROIX INVALIDE"
  print ("Test"+str(i)+" : "+validite)
  #print(c)

#debug
'''c = Cube()
c.scramble(tests[23])
c,mouv = cross_facile(c,[])
print ("Test 24")
print(c)'''


#-------------------------FIN TEST CROIX