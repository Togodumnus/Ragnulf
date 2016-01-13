# Changelog
All notable changes to this project will be documented in this file.
See http://keepachangelog.com

## v1.0.0 - 13/01/2016

### Fixed
- Prise en charge des cubes insolvables

### Added
- Une visualisation ascii des mouvements à effectuer
- Statistiques sur `algo.py`
- Tests unitaires
- Détection et remplacement des formes type "R R" ou "U U'"
  avec `heuristique/`

### Changed
- Un tuto amélioré
- `solve()` respecte l'API demandée
- Étape F2L améliorée
- Optimisation utilisation mémoire

## v0.4.0 - 07/01/2016

### Fixed
- Fix #18. La liste des mouvements était parfois incomplète

### Changed
- Amélioration du tuto

## v0.3.0 - 05/01/2016

### Added
- Résolution complète d'un cube par `poqb.py`
- Sortie animée avec `--tuto`

## v0.2.0 - 16/12/2015

### Added
- Lecture d'un cube par `lecture_cube()` dans `lire_entree.py`
- Ajout d'une fonction `Cube.get_facette(cube, indice)`
- Algorithme de résolution dans `algo.py`.
  Non optimisé, pas encore utilisé dans `poqb.py`.

## v0.1.0 - 01/12/2015

### Added
- Modélisation du Rubik's Cube en petits cubes (après comparaison avec version d'Arnaud)
