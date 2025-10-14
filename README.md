# The Farmer Was Replaced - Scripts d'automatisation

Automatisez votre ferme et optimisez votre progression dans "The Farmer Was Replaced".

## Pourquoi utiliser ces scripts?

Vous en avez marre de gérer manuellement votre ferme? Ces scripts vous permettent de:

- Automatiser complètement votre farming avec gestion intelligente des priorités
- Multiplier votre efficacité grâce à une gestion optimisée des drones
- Résoudre les labyrinthes rapidement avec exploration multi-drones
- Trier et farmer les cactus sans effort
- Récolter les tournesols par niveau de pétales automatiquement

## Installation

1. Copiez tous les fichiers dans votre dossier de sauvegarde du jeu
2. Ouvrez `parameters.py` et ajustez les valeurs selon vos besoins:
   - `WORLD_SIZE`: Taille de votre grille
   - `DRONE_NUMBER`: Nombre de drones disponibles
   - `PLANTS`: Définissez vos objectifs de récolte et priorités

3. Lancez `newMain.py` dans le jeu

## Outils disponibles dans tools.py

### drone_grid(function, parameter)

La fonction la plus puissante du projet. Elle gère automatiquement le spawn et la répartition de vos drones sur toute la grille.

Utilisation:
```python
tools.drone_grid(plant_line, Entities.Carrots)
```

Avantages:
- Spawn automatique du nombre optimal de drones
- Distribution parallèle des tâches
- Gestion intelligente du positionnement
- Compatible avec toutes vos fonctions de farming

### go_to(x, y)

Navigation optimisée qui prend le chemin le plus court en tenant compte du wrapping de la carte.

```python
tools.go_to(10, 5)
```

### priority_crop()

Détermine automatiquement quelle culture planter en fonction de vos objectifs et stocks actuels.

```python
currentCrop = tools.priority_crop()
```

### smart_clear()

Nettoie efficacement toute la ferme avec des drones avant de changer de culture, pour économiser vos graines.

```python
tools.smart_clear()
```

## Modules spécialisés

- **farmModule.py**: Farming automatique de toutes les cultures standard
- **sunflowerModule.py**: Récolte optimisée des tournesols par niveau de pétales
- **mazeModule.py**: Résolution rapide des labyrinthes avec stratégies multiples
- **cactusModule.py**: Culture et tri automatique des cactus
- **bonesModule.py**: Farming d'os avec les dinosaures

## Comment intégrer dans votre ferme existante

Vous avez déjà vos propres scripts? Pas de problème:

1. Importez juste `tools.py` et `parameters.py`
2. Utilisez `tools.drone_grid()` pour remplacer vos boucles manuelles
3. Utilisez `tools.go_to()` pour vos déplacements
4. Configurez `parameters.py` selon vos besoins

Exemple d'intégration:
```python
import tools
import parameters

def ma_fonction_farm():
    tools.drone_grid(ma_ligne_custom, mon_parametre)
```

## Support

Si ces scripts vous aident à progresser dans le jeu, vous pouvez me soutenir:
https://ko-fi.com/thorrdu

## Référence du jeu

Wiki officiel: https://thefarmerwasreplaced.wiki.gg/

