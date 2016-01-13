Tests Ragnulf
============

Tests unitaires pour Ragnulf

# Tests

Les tests sont implémentés avec la librairie par défaut `unittest`.

Pour lancer les tests unitaires :
```python
python -m unittest discover -v
```

Ou, avec `green` (`pip3 install green`), pour avoir un peu de couleurs :
```python
green -vvv
```

Et, avec l'information de `coverage` (`pip3 install coverage`) :
```
green -vvv -r #avec coverage d'installé sur la machine
```

# Le jeu de test

Par défaut, les deux jeux de test sont présents dans
`samples/rotations-sample.json` et `samples/list-sample.json`.

Le premier fichier contient 60 cubes sur lesquels ont a appliqué les 18 mouvements
`{(X, X', X2) | X = (U, R, F, L, B, D)}` avec la librairie nodejs
[cube.js](https://github.com/akheron/cubejs) et sauvegardé le résulat de chacun.

Le second est la liste des `60*18=1080` cubes générés.

Ils ont été générés par `samples/build.js`. On peut lancer la création d'un autre
jeu de test avec `node samples/build.js -o sample.js`.