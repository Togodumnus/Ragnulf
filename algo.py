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

def cross(c):
    '''
    Etape 1 de l'algo CFOP
    Prend le cube en entrée et réalise la première étape de l'algo CFOP
    c'est à dire réalisé une croix sur la face blanche, exemple : 
           X W X
           W W W
           X W X
    X X X  X X X  X X X  X X X
    X X X  X X X  X X X  X X X
    X X X  X X X  X X X  X X X
           X X X
           X X X
           X X X

    :Args:
        c {Cube} l'objet cube, à résoudre

    :Returns:
        {Cube} L'objet cube avec la croix blanche faite 
    '''

def ftl(c):
    '''
    Etape 2 de l'algo CFOP
    Faire les deux "layers", c'est à dire avoir les côtés 
    Vert, Rouge, Bleu et Orange au 2/3 fais, exemple : 
           W W W
           W W W
           W W W
    O O O  G G G  R R R  R R R
    O O O  G G G  R R R  R R R
    X X X  X X X  X X X  X X X
           X X X 
           X X X
           X X X

    :Args:
        c {Cube} l'objet cube, à résoudre

    :Returns:
        {Cube} L'objet cube avec les deux layers de fait
    '''

#Etape 3 de l'algo
def oll(c):


#Etape 4 de l'algo
def pll(c):
