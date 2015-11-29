from Cube import Cube
from utils import colorToCode

def decomposition_faces(str):
    """
    decomposition_faces

    Décompose la chaîne représentant les 54 facettes en 6 faces

    :Args:
        str {String}    chaîne de 54 facettes

    :Returns:
        {Boolean|String}, {List|None}   (error, faces)
                    Liste de 6 liste de 9 éléments (les 6 faces)
                    couleurs codées en entiers
    """

    if not len(str) == 54: #check taille str
        return 'La chaîne ne fait pas 54 caractères', None #returns error
    else:
        faces = [[] for i in range(6)] #init des faces

        for i in range(len(str)):
            case = colorToCode(str[i])
            if i < 9: #face up
                faces[0].append(case)
            elif i > 44: #face down
                faces[5].append(case)
            else:
                i_ = (i - 9) % 12 #on calcule la place du caractère dans
                                  #les 4 faces du milieu
                if i_ < 3: #face left
                    faces[1].append(case)
                elif i_ < 6: #face front
                    faces[2].append(case)
                elif i_ < 9: #face right
                    faces[3].append(case)
                else: # i_ < 12, face back
                    faces[4].append(case)

    return False, faces

def check_faces(faces):
    '''
    check_faces

    Contrôle de la validité des faces passées en paramètes
    On vérifie ici :
        - on a bien 9 facettes par face
        - on a bien une face de chaque couleur (facette du milieu)
        - on a bien 9 facettes pour chacune des 6 couleurs

    :Args:
        faces   {List}      Liste de 6 faces décomposées par decomposition_faces()

    :Returns:
        {Boolean|String}    False ou l'erreur
    '''
    error = False

    l = 6 #nombre de faces
    couleurs_faces = [False] * 6 #vérification de la présence des 6 couleurs
    couleurs = [0] * 6           #comptage du nombre de facettes de chaque couleur

    i = 0 #compteur de face
    while i < l:
        face = faces[i]

        if not len(face) == 9: #on vérifie le nombre de facettes dans la face
            error = 'Face ' + str(i) + ' n\'a pas 9 facettes'
        elif face[4] == None: #on valide la couleur de la face
            error = 'Caractères non autorisés'
        else:
            couleurs_faces[face[4]] = True

            for c in face:
                couleurs[c] += 1 #on compte le nombre de facettes de la couleur `c`

        i += 1

    if not error:
        if not sum(couleurs_faces) == 6: #on a pas une couleur différente par face
            error = 'Chaque face ne possède pas une couleur différente'

        if not couleurs.count(9) == 6: #on a pas 6 couleurs présentes 9 fois, erreur
            error = 'Toutes les couleurs ne sont pas présentes 9 fois'

    return error


def lecture_cube(str_cube):
    '''
    lecture_cube

    Fonction qui permet de lire l'entrée de l'utilisateur.
    Prend une chaîne de 54 caractères et renvoie un objet cube initialisé,
    avec les nombres se rapportant aux couleurs.

    :Args:
        str {String}    chaîne de 54 facettes

    :Returns:
        {Boolean|String}, {Cube}    (error, cube)
                                    Un objet cube initialisé avec les numéros
                                    correspondant à la chaîne de caractères entrée
                                    en paramètre
    '''

    c = Cube()
    error, facesCube = decomposition_faces(str_cube) #on découpe en faces
    if error:
        return error, None

    error = check_faces(facesCube) #on check que les faces sont ok
    if error:
        return error, None


    #Chaque petit cube est codé dans l'objet cube
    #Ils correspondent à toutes les arêtes/coins en commun des différentes faces
    #Exemple : FU = Cube reliant les faces Front et Up

    #Comme nous avons les couleurs et la position de chaque face,
    #nous pouvons attribuer à tous ces cubes leurs couleurs respectives

    insertions = [
        ('FU',  [str_front[1],str_up[7]]),
        ('FRU', [str_front[2],str_right[0],str_up[8]]),
        ('FR',  [str_front[5],str_right[3]]),
        ('FRD', [str_front[8],str_right[6],str_down[2]]),
        ('FD',  [str_front[7],str_down[1]]),
        ('FLD', [str_front[6],str_left[8],str_down[0]]),
        ('FL',  [str_front[3],str_left[5]]),
        ('FLU', [str_front[0],str_left[2],str_up[6]]),

        ('LU',  [str_left[1],str_up[3]]),
        ('LD',  [str_left[7],str_down[3]]),

        ('BU',  [str_back[1],str_up[1]]),
        ('BRU', [str_back[0],str_right[2],str_up[2]]),
        ('BR',  [str_back[3],str_right[5]]),
        ('BRD', [str_back[6],str_right[8],str_down[8]]),
        ('BD',  [str_back[7],str_down[7]]),
        ('BLD', [str_back[8],str_left[6],str_down[6]]),
        ('BL',  [str_back[5],str_left[3]]),
        ('BLU', [str_back[2],str_left[0],str_up[0]]),

        ('RD',  [str_right[7],str_down[5]]),
        ('RU',  [str_right[1],str_up[5]]),
    ]

    #on insert ces petits cubes tant qu'on ne détecte pas de petit
    #cube défaillant

    ok = True
    i = 0
    l = len(insertions)
    while ok and i < l:
        ok = c.edit_cube(insertions[i][0], insertions[i][1])
        i += 1

    return (False, c) if ok else ('Petits cubes invalides', None)

if __name__ == "__main__":

    tests = [
        'AAAA', #erreur de taille
        'YYYYYYYYYOOOBBBRRRGGGOOOBBBRRRGGGOOOBBBRRRGGGWWWWWWWWW', #correct
        #incorrect, mauvais codage
        'VVVVVVVVVOOOBBBRRRGGGOOOBBBRRRGGGOOOBBBRRRGGGWWWWWWWWW',
        #incorrect, toutes les faces ne possède pas une couleur différente
        'YYYYYYYYYOOOOOOOOOBBBBBBBBBRRRRRRRRRGGGGGGGGGWWWWWWWWW',
        #incorrect, on n'a pas 9 facettes de chaque couleur
        'YYYYYYYYYOOOOOOOOOOOOOOOBBBRRRGGGOOOOOOOOOOOOWWWWWWWWW',
        #incorrect, on a un coin BLU OOO, mais non détecté par check_faces()
        'YYYOYGYYYYOOBBBRRRGGYOOOBBBRRRGGGOOOBBBRRRGGGWWWWWWWWW',
        #donné par profs, apparement petits cubes incorrects
        'OGRBWYBGBGYYOYOWOWGRYOOOBGBRRYRBWWWRBWYGROWGRYBRGYWBOG',
        #correct, exemple réel
        'WGWBGGYRBOOBRBYOWGRRBOYYORBWWYROGORRYYGOOWBBYGGWWBWGYR'
    ]

    print('Tests check_faces')
    for test in tests:
        error, f = decomposition_faces(test)
        print(test)
        print('    Erreur :', check_faces(f) if not error else error)

    print('\nTests lecture_cube')
    for test in tests :
        print(test)
        error, cube = lecture_cube(test)
        print('Erreur :', error)
        if not error:
            print(cube)
