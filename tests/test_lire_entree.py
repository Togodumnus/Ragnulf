"""
Unit tests pour lire_entree.py
"""

import unittest
from lire_entree import *

class TestDecompositionFaces(unittest.TestCase):
    """Test de decomposition_faces()"""

    def testTailleType(self):
        """
        decomposition_faces() ne doit accepter que des chaînes
        de 54 caractères
        """
        with self.assertRaises(TypeError):
            decomposition_faces([])
        with self.assertRaises(TypeError):
            decomposition_faces(123)

        with self.assertRaises(ValueError):
            decomposition_faces('mon beau sapin')
        with self.assertRaises(ValueError):
            decomposition_faces('GRBYWYWWORRRBBGWBYOBYWROBBRWOGOGOWGYRGWOROGOGBWBYYGRY1')

    def testDecomposition(self):
        """decomposition_faces() doit faire son job"""

        #on doit avoir 6 faces composées de 9 facettes

        entree = "GRBYWYWWORRRBBGWBYOBYWROBBRWOGOGOWGYRGWOROGOGBWBYYGRYY"
        faces = [
            [3,2,1,5,0,5,0,0,4],
            [2,2,2,0,2,4,0,3,5],
            [1,1,3,1,1,2,2,3,0],
            [0,1,5,0,4,3,4,2,4],
            [4,1,5,4,3,4,3,4,3],
            [1,0,1,5,5,3,2,5,5]
        ]

        result = decomposition_faces(entree)
        self.assertEqual(result, faces)

class TestCheckFaces(unittest.TestCase):


if __name__ == '__main__':
    unittest.main()
