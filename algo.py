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

  c = lecture_cube('WYRGWBROYYGOBWYBGGRWGRGYBRBOBRGOBBYBWWOGOGOOWRROWYRWYY')
  print(c)
