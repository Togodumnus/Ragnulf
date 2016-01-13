import json
from math import sqrt,fabs

def moyenne(liste):
    moyenne = 0
    for i in liste:
        moyenne += i
    return moyenne/len(liste)

def variance(liste):
    variance = 0
    moy = moyenne(liste)
    for i in liste:
        variance += (i-moy)*(i-moy)
    return variance/len(liste)

def ecart_type(liste):
    return sqrt(variance(liste))

def ecart_moyen(liste):
    ecart_moyen = 0
    moy = moyenne(liste)
    for i in liste:
        ecart_moyen += fabs(i-moy)
    return ecart_moyen/len(liste)

def mediane(liste):
    liste.sort()
    if len(liste)%2==0:
        return moyenne([liste[int((len(liste)/2)-1)],liste[int(len(liste)/2)]])
    else: 
        return liste[int(len(liste)/2).__round__(2)]