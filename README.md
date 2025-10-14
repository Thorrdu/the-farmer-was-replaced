# The Farmer Was Replaced - Automation Scripts

Automate your farm and optimize your progression in "The Farmer Was Replaced".

## Why use these scripts?

Tired of manually managing your farm? These scripts allow you to:

- Fully automate your farming with intelligent priority management
- Multiply your efficiency with optimized drone management
- Solve mazes quickly with multi-drone exploration
- Sort and farm cacti effortlessly
- Harvest sunflowers by petal level automatically

## Installation

1. Copy all files to your game save folder
2. Open `parameters.py` and adjust values according to your needs:
   - `WORLD_SIZE`: Your grid size
   - `DRONE_NUMBER`: Number of available drones
   - `PLANTS`: Set your harvest goals and priorities

3. Run `newMain.py` in the game

## Available tools in tools.py

### drone_grid(function, parameter)

The most powerful function in the project. It automatically handles spawning and distributing your drones across the entire grid.

Usage:
```python
tools.drone_grid(plant_line, Entities.Carrots)
```

Benefits:
- Automatic spawning of the optimal number of drones
- Parallel task distribution
- Intelligent positioning management
- Compatible with all your farming functions

### go_to(x, y)

Optimized navigation that takes the shortest path while accounting for map wrapping.

```python
tools.go_to(10, 5)
```

### priority_crop()

Automatically determines which crop to plant based on your goals and current stock.

```python
currentCrop = tools.priority_crop()
```

### smart_clear()

Efficiently clears the entire farm with drones before changing crops, to save your seeds.

```python
tools.smart_clear()
```

## Specialized modules

- **farmModule.py**: Automatic farming of all standard crops
- **sunflowerModule.py**: Optimized sunflower harvest by petal level
- **mazeModule.py**: Fast maze solving with multiple strategies
- **cactusModule.py**: Automatic cactus farming and sorting
- **bonesModule.py**: Bone farming with dinosaurs

## How to integrate into your existing farm

Already have your own scripts? No problem:

1. Just import `tools.py` and `parameters.py`
2. Use `tools.drone_grid()` to replace your manual loops
3. Use `tools.go_to()` for your movements
4. Configure `parameters.py` according to your needs

Integration example:
```python
import tools
import parameters

def my_custom_farm():
    tools.drone_grid(my_custom_line, my_parameter)
```

## Support

If these scripts help you progress in the game, you can support me:
https://ko-fi.com/thorrdu

## Game reference

Official wiki: https://thefarmerwasreplaced.wiki.gg/

