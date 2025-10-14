# The Farmer Was Replaced - Scripts d'automatisation

Scripts Python pour automatiser le gameplay du jeu "The Farmer Was Replaced".

## Description

Ce projet contient une collection de modules optimisés pour gérer automatiquement les différentes tâches du jeu "The Farmer Was Replaced". Les scripts utilisent une gestion centralisée des drones et une architecture modulaire pour maximiser l'efficacité des opérations agricoles et d'exploration.

## Structure du projet

### Modules principaux

- **newMain.py**: Point d'entrée principal qui gère la boucle de jeu et la priorisation des cultures
- **tools.py**: Fonctions utilitaires centralisées incluant la gestion des drones, navigation et priorisation
- **parameters.py**: Configuration centralisée des paramètres de jeu et définitions des plantes

### Modules spécialisés

- **farmModule.py**: Gestion générale des cultures (plantation, récolte, farming)
- **sunflowerModule.py**: Logique spécialisée pour la culture des tournesols avec tri par pétales
- **mazeModule.py**: Résolution de labyrinthes multi-drones avec stratégies right-hand et left-hand
- **cactusModule.py**: Culture et tri des cactus en grille
- **bonesModule.py**: Farming d'os via dinosaures

## Fonctionnalités principales

### Gestion des drones

Utilisation d'un système centralisé `drone_grid()` pour:
- Spawn automatique de drones sur toute la grille
- Distribution parallèle des tâches
- Gestion optimisée des ressources

### Priorisation intelligente

Système de scoring pour déterminer automatiquement la culture prioritaire basé sur:
- Quantités actuelles vs objectifs
- Temps de cycle de croissance
- Disponibilité des ressources

### Optimisations spécifiques

- **Tournesols**: Récolte par niveau de pétales sans tri coûteux
- **Labyrinthes**: Exploration multi-drones avec détection de boucles
- **Cactus**: Tri bidirectionnel optimisé

## Conventions de code

- Variables: camelCase
- Constantes: SNAKE_CASE majuscules
- Modules: organisation par fonctionnalité

## Limitations

Le projet est conçu pour l'interpréteur Python spécifique du jeu, qui présente certaines restrictions:
- Pas d'opérateur ternaire inline
- Pas de `float('inf')`
- Pas de lambda avec arguments par défaut
- Variables d'autres modules considérées comme constantes

## Référence

Basé sur le jeu: https://thefarmerwasreplaced.wiki.gg/

## Auteur

Développé pour automatiser et optimiser le gameplay de "The Farmer Was Replaced".

