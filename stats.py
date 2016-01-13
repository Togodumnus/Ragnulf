from math import sqrt,fabs

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

def ecart_moyen(liste):
	ecart_moyen = 0
	moy = moyenne(liste)
	for i in liste:
		ecart_moyen += fabs(i-moy)
	return ecart_moyen/len(liste)

