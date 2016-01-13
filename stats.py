from math import sqrt

def moyenne (liste):
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

