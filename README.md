![Newcastle Vikings Logo from Wikipedia by Garethom](https://upload.wikimedia.org/wikipedia/commons/3/33/NewcastleVikingsLogo.PNG)

Ragnulf
=======

Résolution d'un Rubik's Cube par la méthode CFOP.

# TL;DR
```bash
python poqb.y --cube OGRBWYBGBGYYOYOWOWGRYOOOBGBRRYRBWWWRBWYGROWGRYBRGYWBOG
```

# Utilisation

## Dépendances

- Python 3
- Numpy (`pip install numpy`).

## Terminal
```bash
python poqb.py [--cube | -c] <cube> [--tuto] [--auto] [--speed | -s] <speed>  [--moves] [--colors]
```

- `--cube <cube>` (optionnel). Un cube à résoudre.

     Par défaut on résout `OGRBWYBGBGYYOYOWOWGRYOOOBGBRRYRBWWWRBWYGROWGRYBRGYWBOG`.

     Format : 54 couleurs parmis {Y, B, R, G, O, W} pour les 54 facettes.

- `-c<cube>` (optionnel). Voir `--cube`.
- `--tuto` (optionnel).

    Activer le mode tutoriel qui affiche la résoltution du cube pas à pas.

- `--auto` (optionnel).

    Avec `--tuto`, avancée automatique.

- `--speed <speed>` (optionnel).

    La vitesse d'avancée avec `--auto` en mouvements par secondes. Défaut 2/sec.

- `-s<speed>` (optionnel). Voir `--speed`.

- `--moves` (optionnel). Afficher la représentation des mouvements à effectuer sur le cube
    en plus du patron coloré.

- `--colors` (optionnel).

    Activer les couleurs ascii sous Windows, par exemple
    dans Git Bash.

## Module
```python
import poqb #import du fichier poqb.py
print(poqb.solve('OGRBWYBGBGYYOYOWOWGRYOOOBGBRRYRBWWWRBWYGROWGRYBRGYWBOG'))
#U2F2F'...
```

# En savoir plus
[:link: Wiki Gitlab](https://gitlab.univ-nantes.fr/E132397K/Ragnulf/wikis/home)

# Tests
Pour lancer les tests unitaires :
```python
python -m unittest discover -v
```

Ou, avec `green` (`pip3 install green`), pour avoir un peu de couleurs :
```python
green -vvv
#ou
green -vvv -r #avec coverage d'installé sur la machine
```

# Membres :
- CLOCHARD Guillaume
- LANGELIER Arnaud
- MARRUCCI Tom
- LEBLANC Jimmy
- DORE Jimmy
- BILLAUD Quentin
