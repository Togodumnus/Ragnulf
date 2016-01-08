![Newcastle Vikings Logo from Wikipedia by Garethom](https://upload.wikimedia.org/wikipedia/commons/3/33/NewcastleVikingsLogo.PNG)

Ragnulf
=======

Résolution d'un Rubik's Cube par la méthode CFOP.

Projet d'Algorithmique et Programmation INFO3 Polytech Nantes.

# TL;DR
```bash
python poqb.y --cube OGRBWYBGBGYYOYOWOWGRYOOOBGBRRYRBWWWRBWYGROWGRYBRGYWBOG
```


# Utilisation

## Terminal
```bash
python poqb.py [--cube | -c] <cube> [--tuto] [--auto] [--speed | -s] <speed> [--colors]
```

- `--cube <cube>` (optionnel). Un cube à résoudre. Par défaut on résout
    `OGRBWYBGBGYYOYOWOWGRYOOOBGBRRYRBWWWRBWYGROWGRYBRGYWBOG`.
    Format : 54 couleurs parmis {Y, B, R, G, O, W} pour les 54 facettes.
- `-c<cube>` (optionnel). Voir `--cube`.
- `--tuto` (optionnel). Activer le mode tutoriel qui affiche la résoltution du
    cube pas à pas.
- `--auto` (optionnel). Avec `--tuto`, avancée automatique.
- `--speed <speed>` (optionnel). La vitesse d'avancée avec `--auto` en
    mouvements par secondes. Défaut 2/sec.
- `-s<speed>` (optionnel). Voir `--speed`.
- `--colors` (optionnel). Activer les couleurs ascii sous Windows, par exemple
    dans Git Bash.

## Module
```python
import poqb #import du fichier poqb.py
print(poqb.solve('OGRBWYBGBGYYOYOWOWGRYOOOBGBRRYRBWWWRBWYGROWGRYBRGYWBOG'))
```


# En savoir plus
[:link: Wiki Gitlab](https://gitlab.univ-nantes.fr/E132397K/Ragnulf/wikis/home)

# Membres :
- CLOCHARD Guillaume
- LANGELIER Arnaud
- MARRUCCI Tom
- LEBLANC Jimmy
- DORE Jimmy
- BILLAUD Quentin
