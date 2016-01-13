import matplotlib.pyplot as plt
from Cube import *
import json
from lire_entree import lecture_cube
from stats import moyenne
from algo import *

JEU_TEST = 'tests/samples/sample-600.json'

with open(JEU_TEST) as data_file: #on parse le jeu de test JSON
        data = json.load(data_file)
        tests = data["cubes"]
        listeNbMouvements = {} # dictionnaire pour stocké en clé : nbMouvement et en valeur : Occurence sur les n tests
        for test in tests: # on parcours tout les cubes
            b,c = lecture_cube(test) 
            c,mouv = algo_cfop(c) # on fais l'algo
            if len(mouv) in listeNbMouvements: # si le nombre de mouvements est deja dans la dictionnaire, on ajoute 1 à son occurence
                listeNbMouvements[len(mouv)] += 1
            else:
                listeNbMouvements[len(mouv)] = 1 # sinon on l'ajoute

listeX = []
listeY = []
for x,y in listeNbMouvements.items(): # on "separe" le dictionnaire en deux liste correspondant aux clés et aux valeurs
    listeX.append(x)
    listeY.append(y)

plt.plot(listeX,listeY) # affichage de la courbe dans pyplot
plt.xlabel('Nombre de mouvements')
plt.ylabel('Occurence sur '+str(len(tests))+' test')
plt.show()
