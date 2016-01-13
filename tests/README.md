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

Par déaut, un jeu de test est présent dans `samples/sample.json`.

Il contient 60 cubes sur lesquels ont a appliqué les 18 mouvements
`{(X, X', X2) | X = (U, R, F, L, B, D)}` avec la librairie nodejs
[cube.js](https://github.com/akheron/cubejs) et sauvegardé le résulat de chacun.

Il a été généré par `samples/build.js`. On peut lancer la création d'un autre
jeu de test avec `node samples/build.js -o sample_bis.js`.

