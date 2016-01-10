
"""
Unit tests pour algo.py
"""

import unittest
import json

from Cube import Cube
from lire_entree import lecture_cube
from algo import algo_cfop

JEU_TEST = './tests/samples/sample.json'


def extract_cubes(data):
    result = []
    for cube, mvts_result in data.items():
        result.append(cube)
        result += data[cube].values()
    return result

class TestAlgo(unittest.TestCase):

    def runTest(self):
        """Test de l'algo CFOP"""
        with open(JEU_TEST) as data_file: #on parse le jeu de test JSON
            data = json.load(data_file)
            cubes = extract_cubes(data) #1140 cubes
            for cube in cubes:
                err, c = lecture_cube(cube)
                if err:
                    raise Error("Erreur lecture_cube \n" + cube)
                err = algo_cfop(c)[0]
                self.assertIsNone(err)

if __name__ == "__main__":
    unittest.main(verbosity=2)
