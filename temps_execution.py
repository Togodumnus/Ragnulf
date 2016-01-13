import time  
import json
from Cube import *
from algo import algo_cfop
from lire_entree import lecture_cube
from stats import *

# Renvois le temps d'éxecution du cube test donné dans poqb.py
def getTimeDefaultCube():
    tmps1=time.clock()
    DEFAULT_CUBE = 'OGRBWYBGBGYYOYOWOWGRYOOOBGBRRYRBWWWRBWYGROWGRYBRGYWBOG'
    b,c = lecture_cube(DEFAULT_CUBE) 
    c,mouv = algo_cfop(c) # on fais l'algo
    tmps2=time.clock()
    return tmps2-tmps1

# Renvois dans une liste le temps d'éxecution des 11400 cubes
def getTimes11400Cubes(): 
    JEU_TEST = 'tests/samples/sample-600.json'
    liste = []
    with open(JEU_TEST) as data_file: #on parse le jeu de test JSON
            data = json.load(data_file)
            tests = data["cubes"]
            for test in tests: # on parcours tout les cubes
                tmps1=time.clock()
                b,c = lecture_cube(test) 
                c,mouv = algo_cfop(c) # on fais l'algo
                tmps2=time.clock()        
                liste.append(tmps2-tmps1)
    return liste

liste = getTimes11400Cubes()

print("Temps éxecution cube test : "+str(getTimeDefaultCube()) +"s") # cube test 
print("Temps éxecution 11400 cubes : "+str(sum(liste)) +"s")
print("Moyenne d'éxecution de 11400 cubes : "+str(moyenne(liste))+"s")
print("Écart type 11400 cubes : "+str(ecart_type(liste)) +"s")