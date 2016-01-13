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

