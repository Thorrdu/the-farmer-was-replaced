import parameters
import tools

def farm_treasures():
	create_maze()
	solve_maze_multi_drone(None)
	
	while get_entity_type() == Entities.Hedge:
		continue
	
def create_maze():
	clear()
	if num_items(Items.Weird_Substance) > parameters.WORLD_SIZE:
		plant(Entities.Bush)
		use_item(Items.Weird_Substance, parameters.WORLD_SIZE * 2 **(num_unlocked(Unlocks.Mazes)))
		use_item(Items.Fertilizer)
	return 1

def solve_maze_multi_drone(previousDirection):
	directions = [North, South, East, West]
	
	if get_entity_type() != Entities.Hedge:
		return 1
	
	for direction in directions:
		if direction == invertDirection(previousDirection):
			pass
		elif can_move(direction):
			while(num_drones() == max_drones()):
				continue
			spawn_drone(tools.drone_func(solve_maze_drone, direction))
	return 1

def solve_maze_drone(direction):	
	move(direction)
	
	entityType = get_entity_type()
		
	if entityType == Entities.Treasure:
		harvest()
	if entityType != Entities.Hedge:
		return 1
		
	solve_maze_multi_drone(direction)
		
def invertDirection(direction):
	invertedDirection = None

	if direction == West:
		invertedDirection = East
	elif direction == East:
		invertedDirection = West
	elif direction == North:
		invertedDirection = South
	elif direction == South:
		invertedDirection = North
	return invertedDirection
	

