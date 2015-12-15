"""
Unit tests pour test_utils.py
"""

import unittest
import numpy
from os import name as os_name
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
        with self.assertRaises(TypeError):
            codeToColor('a')
        with self.assertRaises(TypeError):
            codeToColor(None)
        with self.assertRaises(TypeError):
            codeToColor()

    def testCodeToColorCodes(self):
        """codeToColor()"""

        tests = [
            (0, 'W'),
            (1, 'B'),
            (2, 'R'),
            (3, 'G'),
            (4, 'O'),
            (5, 'Y'),
            (-1, None)
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

class TestColorsHelpers(unittest.TestCase):

    @unittest.skipIf(os_name == 'nt', "Lancé sous Unix")
    def testTermColorsUnix(self):
        """TermColors doit contenir des couleurs ascii"""
        self.assertEqual(TermColors.black, '\033[38;5;232m')

    @unittest.skipIf(not os_name == 'nt', "Lancé sous Windows")
    def testTermColorsWindows(self):
        """TermColors doit être vide"""
        self.assertEqual(TermColors.black, '')

    def testColorize_listError(self):
        """colorize() doit planter si on lui passe une liste trop petite"""

        with self.assertRaises(AssertionError):
            colorize('W', ['lololol'])

    @unittest.skipIf(os_name == 'nt', "Lancé sous Unix")
    def testColorizeUnix_default(self):
        """colorize() doit bien retourner la couleur colorée"""

        tests = [
            ('W', '\033[48;5;255m\033[38;5;232mW\033[m'),
            ('Y', '\033[48;5;220m\033[38;5;232mY\033[m'),
            ('B', '\033[48;5;18mB\033[m'),
            ('R', '\033[48;5;124mR\033[m'),
            ('G', '\033[48;5;22mG\033[m'),
            ('O', '\033[48;5;202mO\033[m'),
            ('a', 'a'),
            (1, 1)
        ]

        for t in tests:
            self.assertEqual(colorize(t[0]), t[1])
            self.assertEqual(colorize(t[0], []), t[1])

    @unittest.skipIf(os_name == 'nt', "Lancé sous Unix")
    def testColorizeUnix_listOption(self):
        """colorize() doit bien utiliser la liste de convertion"""

        convert = ['Yo', 'Yo', 'Yo', 'Yo', 'Yo', 'Yo']
        tests = [
            ('W', '\033[48;5;255m\033[38;5;232mYo\033[m'),
            ('Y', '\033[48;5;220m\033[38;5;232mYo\033[m'),
            ('B', '\033[48;5;18mYo\033[m'),
            ('R', '\033[48;5;124mYo\033[m'),
            ('G', '\033[48;5;22mYo\033[m'),
            ('O', '\033[48;5;202mYo\033[m'),
            ('a', 'a'),
            (1, 1)
        ]

        for t in tests:
            self.assertEqual(colorize(t[0], convert), t[1])

    @unittest.skipIf(not os_name == 'nt', "Lancé sous Windows")
    def testColorizeWindows(self):
        """colorize() ne doit pas retourner de couleurs sous Windows"""

        tests = [
            ('W', 'W'),
            ('Y', 'Y'),
            ('B', 'B'),
            ('R', 'R'),
            ('G', 'G'),
            ('O', 'O'),
            ('a', 'a'),
            (1, 1)
        ]

        for t in tests:
            self.assertEqual(colorize(t[0]), t[1])
            self.assertEqual(colorize(t[0], []), t[1])


if __name__ == '__main__':
    unittest.main(verbosity=2)

