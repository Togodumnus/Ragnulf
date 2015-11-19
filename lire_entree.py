from Cube import Cube
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




'''
# Str de 48 caractères à transformer en 21 cubes de 2 ou 3 caractères. 

 
 Ne pas oublier
   Convention des couleurs des faces :
        Down  - White
        Front - Blue
        Right - Red
        Back  - Green
        Left  - Orange
        Up    - Yellow




'''
def data_cube_dictionnaire(str_cube):
    c = Cube()
    facesCube = faces(str_cube)
    #On a les 6 faces mais on ne sait pas quelle face est up, down ..

    print(facesCube)
    
    str_left = None  # Orange 4
    str_front = None # Blue   1
    str_right = None # Red    2
    str_back = None # Green   3
    str_down = None # White   0
    str_up = None  # Yellow   5

    for face in facesCube:
        if face[4] == 'O':
            str_left = face
        elif face[4] == 'B':
            str_front = face
        elif face[4] == 'R':
            str_right = face
        elif face[4] == 'G'
            str_back = face
        elif face[4] = 'W'
            str_down = face
        elif face[4] == 'Y'
            str_up = face
        else :
            return None
    






if __name__ == "__main__":

    str_cube = "OGRBWYBGBGYYOYOWOWGRYOOOBGBRRYRBWWWRBWYGROWGRYBRGYWBOG"
    cube = data_cube_dictionnaire(str_cube)
