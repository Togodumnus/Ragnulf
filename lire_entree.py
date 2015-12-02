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

    #1. Découpage des faces de la chaîne en entrée

    c = Cube()
    error, faces = decomposition_faces(str_cube) #on découpe en faces
    if error:
        return error, None

    #2. Vérification des faces

    error = check_faces(faces) #on check que les faces sont ok
    if error:
        return error, None

    #3. Remplir le rubik's cube

    #Chaque petit cube est codé dans l'objet cube
    #Ils correspondent à toutes les arêtes/coins en commun des différentes faces
    #Exemple : FU = Cube reliant les faces Front et Up

    #Comme nous avons les couleurs et la position de chaque face,
    #nous pouvons attribuer à tous ces cubes leurs couleurs respectives

    insertions = [
        ('FU',  [faces[2][1], faces[0][7]]),
        ('FRU', [faces[2][2], faces[3][0], faces[0][8]]),
        ('FR',  [faces[2][5], faces[3][3]]),
        ('FRD', [faces[2][8], faces[3][6], faces[5][2]]),
        ('FD',  [faces[2][7], faces[5][1]]),
        ('LFD', [faces[1][8], faces[2][6], faces[5][0]]),
        ('FL',  [faces[2][3], faces[1][5]]),
        ('LFU', [faces[1][2], faces[2][0], faces[0][6]]),

        ('LU',  [faces[1][1], faces[0][3]]),
        ('LD',  [faces[1][7], faces[5][3]]),

        ('BU',  [faces[4][1], faces[0][1]]),
        ('RBU', [faces[3][2], faces[4][0], faces[0][2]]),
        ('BR',  [faces[4][3], faces[3][5]]),
        ('RBD', [faces[3][8], faces[4][6], faces[5][8]]),
        ('BD',  [faces[4][7], faces[5][7]]),
        ('BLD', [faces[4][8], faces[1][6], faces[5][6]]),
        ('BL',  [faces[4][5], faces[1][3]]),
        ('BLU', [faces[4][2], faces[1][0], faces[0][0]]),

        ('RD',  [faces[3][7], faces[5][5]]),
        ('RU',  [faces[3][1], faces[0][5]]),
    ]

    #on insert ces petits cubes tant qu'on ne détecte pas de petit
    #cube défaillant

    ok = True
    i = 0
    l = len(insertions)
    while ok and i < l:
        ok = c.edit_cube(insertions[i][0], insertions[i][1])
        i += 1

    if not ok: #si erreur dans les petits cubes, on ne va pas plus loin
        return ('Petits cubes invalides', None)

    #4. Mettre le cube dans la bonne position
    #(face blanche en bas, bleue en front)

    #les couleurs de chaque faces
    couleurs_faces = [face[4] for face in faces]

    v = (couleurs_faces.index(0), couleurs_faces.index(1))

    if v[0] == 0: #si la face blanche est sur U
                  # alors la face bleue est sur L, F, R ou B
        c.rot_UF()
        c.rot_UF()
        if not v[1] == 4: #on place la face bleue, sauf si elle est déjà sur F
            for _ in range(v[1]):
                c.rot_FR()
    elif v[0] == 5: #la face blanche est placée
        #on place la face bleue, sauf si elle est déjà sur F
        if v[1] == 1:
            c.rot_FR() #on tourne
        for j in [3, 4]:
            if v[1] == j or v[1] == j:
                for x in range(6 - j):
                    c.rot_FR() #on tourne
    else: #la face blanche est sur L, F, R ou B
        #on place la face blanche sur F
        if v[0] == 1:
            c.rot_FR() #on tourne
        else:
            for j in [3, 4]:
                if v[0] == j or v[0] == j:
                    for x in range(6 - j):
                        c.rot_FR() #on tourne
        c.rot_UF() #on descend la face blanche sur D

        #on place la face bleue
        #si elle était sur U, elle est à la bonne place maintenant
        if v[1] == 5: #si elle était sur D, elle est sur B maintenant
            c.rot_FR()
            c.rot_FR()
        #on s'intéresse aux cas pù la face bleue est sur L ou R
        #cas où on est sur R maintenant
        elif v[1] == v[0] + 1 or (v[0], v[1]) == (4, 1):
            for x in range(3):
                c.rot_FR()
        #cas où on est sur L maintenant
        elif v[1] == v[0] - 1 or (v[0], v[1]) == (1, 4):
            c.rot_FR()

    return (False, c)

if __name__ == "__main__":

    tests = [
        'AAAA', #erreur de taille
        #incorrect, mauvais codage
        'VVVVVVVVVOOOBBBRRRGGGOOOBBBRRRGGGOOOBBBRRRGGGWWWWWWWWW',
        #incorrect, toutes les faces ne possède pas une couleur différente
        'YYYYYYYYYOOOOOOOOOBBBBBBBBBRRRRRRRRRGGGGGGGGGWWWWWWWWW',
        #incorrect, on n'a pas 9 facettes de chaque couleur
        'YYYYYYYYYOOOOOOOOOOOOOOOBBBRRRGGGOOOOOOOOOOOOWWWWWWWWW',
        #incorrect, on a un coin BLU OOO, mais non détecté par check_faces()
        'YYYOYGYYYYOOBBBRRRGGYOOOBBBRRRGGGOOOBBBRRRGGGWWWWWWWWW',
        'YYYYYYYYYOOOBBBRRRGGGOOOBBBRRRGGGOOOBBBRRRGGGWWWWWWWWW', #correct
        'WWWWWWWWWOOOGGGRRRBBBOOOGGGRRRBBBOOOGGGRRRBBBYYYYYYYYY', #correct
        'YYYYYYYYYGGGOOOBBBRRRGGGOOOBBBRRRGGGOOOBBBRRRWWWWWWWWW', #correct
        'GGGGGGGGGOOOYYYRRRWWWOOOYYYRRRWWWOOOYYYRRRWWWBBBBBBBBB', #correct
        'RRRRRRRRRYYYBBBWWWGGGYYYBBBWWWGGGYYYBBBWWWGGGOOOOOOOOO', #correct
        #donné par profs
        'OGRBWYBGBGYYOYOWOWGRYOOOBGBRRYRBWWWRBWYGROWGRYBRGYWBOG',
        #correct, exemple réel
        'WGWBGGYRBOOBRBYOWGRRBOYYORBWWYROGORRYYGOOWBBYGGWWBWGYR'
    ]

    print('Tests check_faces')
    print('=================')
    for test in tests:
        error, f = decomposition_faces(test)
        print(test)
        print('    Erreur :', check_faces(f) if not error else error)

    print('\nTests lecture_cube')
    print('====================')
    for test in tests :
        print(test)
        error, cube = lecture_cube(test)
        print('    Erreur :', error)
        if not error:
            print(cube)
