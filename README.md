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

### check_till()

Checks if the current ground is tilled, and tills it if necessary. Essential before planting.

```python
tools.check_till()
```

## Standalone functions for custom scripts

### farm_line(cropType)

Harvests and replants an entire line. Perfect for creating custom farming patterns.

```python
import farmModule

def my_custom_farm():
    for row in range(10):
        farmModule.farm_line(Entities.Carrots)
        move(North)
```

### plant_line(cropType)

Plants a specific crop across an entire line. Handles special cases like Trees with Bush companions.

```python
import farmModule

farmModule.plant_line(Entities.Tree)
```

### plant_crop(cropType)

Smart planting function that handles all the requirements for a crop:
- Automatically tills the ground if needed
- Waters until optimal level
- Applies fertilizer for pumpkins
- Replants dead pumpkins automatically

```python
import farmModule

tools.check_till()
farmModule.plant_crop(Entities.Pumpkin)
```

Usage example combining multiple functions:
```python
import tools
import farmModule

def my_selective_harvest():
    for row in range(tools.worldSize):
        for col in range(tools.worldSize):
            if can_harvest():
                harvest()
                farmModule.plant_crop(Entities.Carrots)
            move(East)
        move(North)
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

