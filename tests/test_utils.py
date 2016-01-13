"""
Unit tests pour test_utils.py
"""

import unittest
import numpy
from os import name as os_name

from utils import *
from Cube import Cube

class TestNumpyArray(unittest.TestCase):

    def runTest(self):
        """Array() doit créer un array numpy"""
        self.assertIsInstance(Array([]), numpy.ndarray)
        self.assertTrue(numpy.array_equal(Array([1, 2, 3]), [1, 2, 3]))

class TestColorsConvertions(unittest.TestCase):
    """Test des fonctions de convertions des couleurs"""

    def testCodeToColorTypes(self):
        """codeToColor() demande un int entre 0 et 6 en param"""

        with self.assertRaises(TypeError):
            codeToColor(1.0)
        with self.assertRaises(TypeError):
            codeToColor('a')
        with self.assertRaises(TypeError):
            codeToColor(None)
        with self.assertRaises(TypeError):
            codeToColor()

        with self.assertRaises(ValueError):
            colorToCode(6)
        with self.assertRaises(ValueError):
            colorToCode(-1)

    def testCodeToColorCodes(self):
        """codeToColor() doit renvoyer les bonnes valeurs"""

        tests = [
            (0, 'W'),
            (1, 'B'),
            (2, 'R'),
            (3, 'G'),
            (4, 'O'),
            (5, 'Y'),
        ]

        for t in tests:
            self.assertEqual(codeToColor(t[0]), t[1])

    def testColorToCodeType(self):
        """
        colorToCode() ne doit accèpter qu'un caractère
        dans {'W', 'B', 'R', 'G', 'O', 'Y'}
        """
        with self.assertRaises(ValueError):
            colorToCode(1)
        with self.assertRaises(ValueError):
            colorToCode(None)
        with self.assertRaises(ValueError):
            colorToCode([])

        with self.assertRaises(ValueError):
            colorToCode('A')

    def testColorToCode(self):
        """colorToCode() doit renvoyer les bonnes valeurs"""

        tests = [
            ('W', 0),
            ('B', 1),
            ('R', 2),
            ('G', 3),
            ('O', 4),
            ('Y', 5)
        ]

        for t in tests:
            self.assertEqual(colorToCode(t[0]), t[1])

    def testCodeToGroupType(self):
        """codeToGroup() ne doit accèpter qu'un int entre 0 et 6"""
        with self.assertRaises(ValueError):
            codeToGroup(-1)
        with self.assertRaises(ValueError):
            codeToGroup(6)
        with self.assertRaises(ValueError):
            codeToGroup('a')

    def testCodeToGroup(self):
        """codeToGroup()"""

        tests = [
            (0, 0),
            (5, 0),
            (2, 1),
            (4, 1),
            (1, 2),
            (3, 2),
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

class TestCroixValide(unittest.TestCase):

    def runTest(self):
        """croix_valide() doit faire son job"""

        c = Cube()
        self.assertTrue(croix_valide(c))
        c.rot_F()
        self.assertFalse(croix_valide(c))

class TestFtlValide(unittest.TestCase):

    def runTest(self):
        """ftl_valide() doit faire son job"""

        c = Cube()
        self.assertTrue(ftl_valide(c))
        c.rot_F()
        self.assertFalse(ftl_valide(c))

if __name__ == '__main__':
    unittest.main(verbosity=2)
