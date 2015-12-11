"""
Unit tests pour test_utils.py
"""

import unittest
import numpy
from utils import *

class TestNumpyArray(unittest.TestCase):
    """Array() doit créer un array numpy"""

    def runTest(self):
        self.assertIsInstance(Array([]), numpy.ndarray)
        self.assertTrue(numpy.array_equal(Array([1, 2, 3]), [1, 2, 3]))

class TestColorsConvertions(unittest.TestCase):
    """Test des fonctions de convertions des couleurs"""

    def testCodeToColorTypes(self):
        """codeToColor() demande un int en param"""

        with self.assertRaises(TypeError):
            codeToColor(1.0)
            codeToColor('a')
            codeToColor(None)
            codeToColor()

    def testCodeToColorCodes(self):
        """codeToColor()"""

        tests = [
            (0, 'W'),
            (1, 'B'),
            (2, 'R'),
            (3, 'G'),
            (4, 'O'),
            (5, 'Y')
        ]

        for t in tests:
            self.assertEqual(codeToColor(t[0]), t[1])

    def testColorToCode(self):
        """colorToCode()"""

        tests = [
            ('W', 0),
            ('B', 1),
            ('R', 2),
            ('G', 3),
            ('O', 4),
            ('Y', 5),

            ('a', None),
            (0, None),
            (None, None)
        ]

        for t in tests:
            self.assertEqual(colorToCode(t[0]), t[1])

    def testCodeToGroup(self):
        """codeToGroup()"""

        tests = [
            (0, 0),
            (5, 0),
            (2, 1),
            (4, 1),
            (1, 2),
            (3, 2),
            ('a', None),
            (-1, None),
            (None, None),
        ]

        for t in tests:
            self.assertEqual(codeToGroup(t[0]), t[1])

if __name__ == '__main__':
    unittest.main(verbosity=2)

