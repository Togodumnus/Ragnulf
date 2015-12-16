"""
Unit tests pour Cube.py
"""

import unittest
import numpy
import json

from Cube import *
from lire_entree import lecture_cube

JEU_TEST = './tests/samples/sample.json'

ROTATIONS = [
    "U", "Ui", "U2", "L", "Li", "L2",
    "F", "Fi", "F2", "R", "Ri", "R2",
    "B", "Bi", "B2", "D", "Di", "D2"
]


class TestCubeSimple(unittest.TestCase):
    """Test de Cube() -- part 1"""

    def setUp(self):
        self.cube = Cube() #un cube résolu

    def tearDown(self):
        self.cube = None

    def testCubes(self):
        """Un Cube() doit posséder tous les petits cubes"""

        keysExpected = [
            #1ère couronne
            'FU' ,
            'FRU',
            'RU' ,
            'RBU',
            'BU' ,
            'BLU',
            'LU' ,
            'LFU',

            #2ème couronne
            'FR' ,
            'BR' ,
            'BL' ,
            'FL' ,

            #3ème couronne
            'FD' ,
            'FRD',
            'RD' ,
            'RBD',
            'BD' ,
            'BLD',
            'LD' ,
            'LFD',
        ]

        self.assertListEqual(
            sorted(keysExpected),
            sorted(list(self.cube.cubes.keys()))
        )

    def testCubesValues(self):
        """Un cube doit être résolu par défault"""

        cubes = [
            #1ère couronne
            ('FU' , [1, 5]),
            ('FRU', [1, 2, 5]),
            ('RU' , [2, 5]),
            ('RBU', [2, 3, 5]),
            ('BU' , [3, 5]),
            ('BLU', [3, 4, 5]),
            ('LU' , [4, 5]),
            ('LFU', [4, 1, 5]),

            #2ème couronne
            ('FR' , [1, 2]),
            ('BR' , [3, 2]),
            ('BL' , [3, 4]),
            ('FL' , [1, 4]),

            #3ème couronne
            ('FD' , [1, 0]),
            ('FRD', [1, 2, 0]),
            ('RD' , [2, 0]),
            ('RBD', [2, 3, 0]),
            ('BD' , [3, 0]),
            ('BLD', [3, 4, 0]),
            ('LD' , [4, 0]),
            ('LFD', [4, 1, 0]),
        ]

        for cube, facettes in cubes:
            self.assertTrue(numpy.array_equal(self.cube.cubes[cube], facettes))

    def testGetFacettes(self):
        """Cube.get_facettes() doit retourner la bonne facette"""

        cubes = [
            #1ère couronne
            ('FU' , Array([1, 5])),
            ('FRU', Array([1, 2, 5])),
            ('RU' , Array([2, 5])),
            ('RBU', Array([2, 3, 5])),
            ('BU' , Array([3, 5])),
            ('BLU', Array([3, 4, 5])),
            ('LU' , Array([4, 5])),
            ('LFU', Array([4, 1, 5])),

            #2ème couronne
            ('FR' , Array([1, 2])),
            ('BR' , Array([3, 2])),
            ('BL' , Array([3, 4])),
            ('FL' , Array([1, 4])),

            #3ème couronne
            ('FD' , Array([1, 0])),
            ('FRD', Array([1, 2, 0])),
            ('RD' , Array([2, 0])),
            ('RBD', Array([2, 3, 0])),
            ('BD' , Array([3, 0])),
            ('BLD', Array([3, 4, 0])),
            ('LD' , Array([4, 0])),
            ('LFD', Array([4, 1, 0])),
        ]

        for cube, facettes in cubes:
            for index, facette in enumerate(facettes):
                self.assertEqual(self.cube.get_facette(cube, index), facette)

    def testEditCubeException(self):
        """Cube.edit_cube() doit accepter uniquement des cubes"""

        with self.assertRaises(ValueError):
            self.cube.edit_cube('abc', [0, 1])
        with self.assertRaises(ValueError):
            self.cube.edit_cube(0, [0, 1])
        with self.assertRaises(ValueError):
            self.cube.edit_cube(None, [0, 1])

    def testEditCubeGroup(self):
        """
        Cube.edit_cube() doit s'assurer qu'un même groupe de couleurs
        n'est pas présent plus d'une fois
        """
        with self.assertRaises(ValueError):
            self.cube.edit_cube('FRU', [0, 1, 0])
        with self.assertRaises(ValueError):
            self.cube.edit_cube('FRU', [2, 2, 2])
        with self.assertRaises(ValueError):
            self.cube.edit_cube('FRU', [0, 5, 5])

    def testEditCubeGroup(self):
        """Cube.edit_cube() doit planter si problème de taille de cube"""
        with self.assertRaises(ValueError):
            self.cube.edit_cube('FRU', [0, 1])
        with self.assertRaises(ValueError):
            self.cube.edit_cube('FU', [0, 1, 2])

    def testEditCubeCouleur(self):
        """Cube.edit_cube() ne doit accèpter que des couleurs"""
        with self.assertRaises(ValueError):
            self.cube.edit_cube('FRU', [0, 1, 8])

    def testEditCubeEdit(self):
        """Cube.edit_cube() doit faire son job"""
        self.cube.edit_cube('FRU', [0, 1, 2])
        self.assertTrue(numpy.array_equal(self.cube.cubes['FRU'], [0, 1, 2]))

    def testCubeContientCouleur(self):
        """Cube.cube_contient_couleur() doit faire son job"""
        self.assertTrue(self.cube.cube_contient_couleur('FRU', 1, 2, 5))
        self.assertFalse(self.cube.cube_contient_couleur('FRU', 0, 2, 5))
        self.assertTrue(self.cube.cube_contient_couleur('FR', 1, 2))
        self.assertFalse(self.cube.cube_contient_couleur('FR', 19, 2))


class TestCubeRotations(unittest.TestCase):
    """Test de Cube() -- part 3"""

def addTestRotation(testCase, rot, jeuTest):
    """
    addTestRotation

    Ajoute les tests des rotations sur TestCubeRotations.
    Comme c'est la même logique pour les 18 rotations,
    on crée les méthodes dynamiquement.

    :Args:
        testCase    {Class}     TestCubeRotations
        rot         {String}    Rotation
        jeuTest     {Dic}       Le json de build.js parsé
    """

    def cube_testRotation(self): #le test de la rotation rot

        for cube, moves in jeuTest.items(): #pour tous les cubes
            result = moves[rot]     #le résulat attendu
            err, c = lecture_cube(cube)  #on lit le cube

            self.assertFalse(err)

            #on applique la rotation
            rotation = getattr(c, 'rot_' + rot)
            rotation()

            #on check si c'est bien ce qui est attendu
            line = c.to_line(colors=False)
            self.assertEqual(
                line,
                result,
                'rot_' + rot + ' (cube ' + cube + '): '
                    + line + ' != ' + result
            )

    #on ajoute la méthode à TestCubeRotations
    cube_testRotation.__doc__ = "Cube.rot_" + rot \
        + "() doit fonctionner correctement"

    cube_testRotation.__name__ = "testRotation" + rot
    setattr(testCase, cube_testRotation.__name__, cube_testRotation)

with open(JEU_TEST) as data_file: #on parse le jeu de test JSON
    data = json.load(data_file)
    for rot in ROTATIONS:
        #double rotations pas encore dispo

        #on ajoute une méthode à TestCubeRotations
        #pour chaque rotation
        addTestRotation(TestCubeRotations, rot, data)

# class TestBuildFace(unittest.TestCase):

if __name__ == '__main__':
    unittest.main()

