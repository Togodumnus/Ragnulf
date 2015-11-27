from utils import Array, codeToColor
from numpy import copy as np_copy

class Cube():
	"""
	Cube

	La structure de donnée modélisant un cube ainsi que les fonctions de
	rotations qui s'y appliquent

	@see https://gitlab.univ-nantes.fr/E132397K/Ragnulf/issues/4 pour
	l'histoirique des choix effectués

	Codage des couleurs :
	    White  (W) = 0
	    Blue   (B) = 1
	    Red    (R) = 2
	    Green  (G) = 3
	    Orange (0) = 4
	    Yellow (Y) = 5

	Convention des couleurs des faces :
	    Down  - White
	    Front - Blue
	    Right - Red
	    Back  - Green
	    Left  - Orange
	    Up    - Yellow
	"""

	def __init__(self):
		"""
		__init__

		Création d'une nouvelle instance de Cube
		"""

		self.cubes = Array( [ 5,5,5,
							  5,  5,
							  5,5,5,
					   4,4,4, 1,1,1, 2,2,2, 3,3,3,
					   4,  4, 1,  1, 2,  2, 3,  3,
					   4,4,4, 1,1,1, 2,2,2, 3,3,3,
							  0,0,0,
							  0,  0,
							  0,0,0] )


	def __str__(self):
		"""
		On veut retourner une chaîne du genre:
		           O G R
		           B Y Y
		           B G B
		    G Y Y  O Y O  W O W  G R Y
		    O O O  B B B  R R Y  R G W
		    W W R  B W Y  G R O  W G R
		           Y B R
		           G W W
		           B O G
		"""

		#Un espace pour constuire le patro ci-dessus
		space = [' ']

		#Une lignes d'espaces pour les blocs vides du patron ci-dessus
		empty = space * 3


		up = [
			[self.cubes[0],  self.cubes[1],  self.cubes[2]],
			[self.cubes[3],       5,         self.cubes[4]],
			[self.cubes[5],  self.cubes[6],  self.cubes[7]],
		]

		left = [
			[self.cubes[8],  self.cubes[9],  self.cubes[10]],
			[self.cubes[20],      4,         self.cubes[21]],
			[self.cubes[28], self.cubes[29], self.cubes[30]],
		]

		front = [
			[self.cubes[11], self.cubes[12], self.cubes[13]],
			[self.cubes[22],      1,         self.cubes[23]],
			[self.cubes[31], self.cubes[32], self.cubes[33]],
		]

		right = [
			[self.cubes[14], self.cubes[15], self.cubes[16]],
			[self.cubes[24],      2,         self.cubes[25]],
			[self.cubes[34], self.cubes[35], self.cubes[36]],
		]

		back = [
			[self.cubes[17], self.cubes[18], self.cubes[19]],
			[self.cubes[26],      3,         self.cubes[27]],
			[self.cubes[37], self.cubes[38], self.cubes[39]],
		]

		down = [
			[self.cubes[40], self.cubes[41], self.cubes[42]],
			[self.cubes[43],      0,         self.cubes[44]],
			[self.cubes[45], self.cubes[46], self.cubes[47]],
		]



		#On convertit tous les entiers en la couleur qui leur correspond
		for face in [up, left, front, right, back, down]:
			for ligne in range(3):
				for c in range(3):
					#pour chaque case de chaque ligne de chaque face
					face[ligne][c] = codeToColor(face[ligne][c])

		result = [] #tableau de toutes les lignes à afficher

		#les 3 premières lignes, il n'y a que la face up
		for i in range(3):
			result.append(empty + space + up[i] + space + empty + space + empty)

		#les 3 lignes suivantes, il y a left, front, right et back
		for i in range(3):
			result.append(left[i] + space + front[i] + space + right[i] + \
					space + back[i])

		#les 3 dernières lignes, il y a que la face down
		for i in range(3):
			result.append(empty + space + down[i] + space + empty)

		return '\n'.join(''.join(l) for l in result) #on convertit la liste en chaîne

	def rot_L(self):
		"""
		rot_L

		Rotation de la face gauche (Left)
		"""

		self.cubes[8],  self.cubes[9],  self.cubes[10],  \
		self.cubes[20],                 self.cubes[21],  \
		self.cubes[28], self.cubes[29], self.cubes[30] = \
		self.cubes[28], self.cubes[20], self.cubes[8],   \
		self.cubes[29],                 self.cubes[9],   \
		self.cubes[30], self.cubes[21], self.cubes[10] 

		self.cubes[0],  self.cubes[3],   self.cubes[5],   \
		self.cubes[11], self.cubes[22],  self.cubes[31],  \
		self.cubes[40], self.cubes[43],  self.cubes[45],  \
		self.cubes[17], self.cubes[26],  self.cubes[37] = \
		self.cubes[37], self.cubes[26],  self.cubes[17],  \
		self.cubes[0],  self.cubes[3],   self.cubes[5],   \
		self.cubes[11], self.cubes[22],  self.cubes[31],  \
		self.cubes[45], self.cubes[43],  self.cubes[40]

	def rot_Li(self):
		"""
		rot_Li

		Rotation inverse de la face gauche (Left)
		"""

		self.cubes[8],  self.cubes[9],  self.cubes[10],  \
		self.cubes[20],                 self.cubes[21],  \
		self.cubes[28], self.cubes[29], self.cubes[30] = \
		self.cubes[10], self.cubes[12], self.cubes[15],  \
		self.cubes[9],                  self.cubes[14],  \
		self.cubes[8],  self.cubes[11], self.cubes[13] 

		self.cubes[0],  self.cubes[3],   self.cubes[5],   \
		self.cubes[16], self.cubes[19],  self.cubes[21],  \
		self.cubes[40], self.cubes[43],  self.cubes[45],  \
		self.cubes[34], self.cubes[36],  self.cubes[39] = \
		self.cubes[39], self.cubes[36],  self.cubes[34],  \
		self.cubes[0],  self.cubes[3],   self.cubes[5],   \
		self.cubes[16], self.cubes[19],  self.cubes[21],  \
		self.cubes[45], self.cubes[43],  self.cubes[40]




if __name__ == '__main__':

	# Exemple d'utilisation du Cube
	c = Cube() #par défaut, ce cube est résolu
	print(c)
	c.rot_L()
	print(c)
