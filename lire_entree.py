from Cube import Cube
from utils import Array,colorToCode
# Analyse de l'entrée pour modéliser le cube par la suite
# Entrée sous la forme : 
# cube = 'OGRBWYBGBGYYOYOWOWGRYOOOBGBRRYRBWWWRBWYGROWGRYBRGYWBOG'




def faces(str):
    """
    faces

    Décompose la chaîne représentant les 54 facettes en 6 faces

    :Args:
        str {String}    chaîne de 54 facettes

    :Returns:
        {List}          Liste de 6 liste de 9 éléments (les 6 faces)
    """

    faces = [[] for i in range(6)] #init des faces

    for i in range(len(str)):
        if i < 9: #face up
            faces[0].append(str[i])
        elif i > 44: #face down
            faces[5].append(str[i])
        else:
            i_ = (i - 9) % 12 #on calcule la place du caractère dans
                              #les 4 faces du milieu
            if i_ < 3: #face left
                faces[1].append(str[i])
            elif i_ < 6: #face front
                faces[2].append(str[i])
            elif i_ < 9: #face right
                faces[3].append(str[i])
            else: # i_ < 12, face back
                faces[4].append(str[i])

    return faces





def data_cube_dictionnaire(str_cube):
    '''
    data_cube_dictionnaire 

    Prend une chaîne de 54 caractères et renvoie un objet cube initialisé, avec les nombres se rapportant aux couleurs
    Fonction qui permet de lire l'entrée de l'utilisateur
 
    :Args:
        str{String} chaîne de 54 facettes

    :Returns:
        {Cube} Un objet cube initialisé avec les numéros correspondant à la chaîne de caractères rentrée en paramètre

    '''
    c = Cube()
    facesCube = faces(str_cube)
    #On a les 6 faces mais on ne sait pas quelle face est up, down ..
    
    str_left = None  # Orange 4
    str_front = None # Blue   1
    str_right = None # Red    2
    str_back = None # Green   3
    str_down = None # White   0
    str_up = None  # Yellow   5

    #On attribue à chaque face une position dans le cube : left, right, front, back, up ou down
    # en fonction de la couleur centrale que doit avoir chaque face
    for face in facesCube:
        if face[4] == 'O': # left : orange
            str_left = face
        elif face[4] == 'B': # front : blue
            str_front = face
        elif face[4] == 'R': # right : red
            str_right = face
        elif face[4] == 'G': # back : green
            str_back = face
        elif face[4] == 'W': # down : white
            str_down = face
        elif face[4] == 'Y': # up : yellow
            str_up = face
        else :
            return None


    # Chaque petit cube est codé dans l'objet cube
    # Ils correspondent à toutes les arêtes en commun des différentes faces
    # Exemple : FU = Cube reliant les faces Front et Up
    # Comme nous avons les couleurs et la position de chaque face, nous pouvons attribuer à tous ces cubes leurs couleurs respectives

    c.cubes['FU'] = Array([colorToCode(str_front[1]),colorToCode(str_up[7])])
    c.cubes['FRU'] = Array([colorToCode(str_front[2]),colorToCode(str_right[0]),colorToCode(str_up[8])])
    c.cubes['FR'] = Array([colorToCode(str_front[5]),colorToCode(str_right[3])])
    c.cubes['FRD'] = Array([colorToCode(str_front[8]),colorToCode(str_right[6]),colorToCode(str_down[2])])
    c.cubes['FD'] = Array([colorToCode(str_front[7]),colorToCode(str_down[1])])
    c.cubes['FLD'] = Array([colorToCode(str_front[6]),colorToCode(str_left[8]),colorToCode(str_down[0])])
    c.cubes['FL'] = Array([colorToCode(str_front[3]),colorToCode(str_left[5])])
    c.cubes['FLU'] = Array([colorToCode(str_front[0]),colorToCode(str_left[2]),colorToCode(str_up[6])])

    c.cubes['LU'] = Array([colorToCode(str_left[1]),colorToCode(str_up[3])])
    c.cubes['LD'] = Array([colorToCode(str_left[7]),colorToCode(str_down[3])])

    c.cubes['BU'] = Array([colorToCode(str_back[1]),colorToCode(str_up[1])])
    c.cubes['BRU'] = Array([colorToCode(str_back[0]),colorToCode(str_right[2]),colorToCode(str_up[2])])
    c.cubes['BR'] = Array([colorToCode(str_back[3]),colorToCode(str_right[5])])
    c.cubes['BRD'] = Array([colorToCode(str_back[6]),colorToCode(str_right[8]),colorToCode(str_down[8])])
    c.cubes['BD'] = Array([colorToCode(str_back[7]),colorToCode(str_down[7])])
    c.cubes['BLD'] = Array([colorToCode(str_back[8]),colorToCode(str_left[6]),colorToCode(str_down[6])])
    c.cubes['BL'] = Array([colorToCode(str_back[5]),colorToCode(str_left[3])])
    c.cubes['BLU'] = Array([colorToCode(str_back[2]),colorToCode(str_left[0]),colorToCode(str_up[0])])

    c.cubes['RU'] = Array([colorToCode(str_right[1]),colorToCode(str_up[5])])
    c.cubes['RD'] = Array([colorToCode(str_right[7]),colorToCode(str_down[5])])

    return c

if __name__ == "__main__":

    str_cube = "OGRBWYBGBGYYOYOWOWGRYOOOBGBRRYRBWWWRBWYGROWGRYBRGYWBOG"
    cube = data_cube_dictionnaire(str_cube)
    print(cube)
