import parameters
import tools

def farm_treasures():
	create_maze()
	solve_maze_multi_drone()

def create_maze():
	clear()
	plant(Entities.Bush)
	
	while get_entity_type() == Entities.Bush:
		if num_items(Items.Weird_Substance) > parameters.WORLD_SIZE:
			use_item(Items.Weird_Substance, parameters.WORLD_SIZE * 2 * num_unlocked(Unlocks.Mazes))
			return 1
		
		if can_harvest():
			harvest()
			plant(Entities.Bush)
		
		if num_items(Items.Fertilizer) == 0:
			return 0
		
		use_item(Items.Fertilizer)
	
	return 1

def solve_maze():
	direction = West
	currentPos = tools.get_position()
	
	while True:
		move(direction)
		
		newPos = tools.get_position()
		
		if currentPos["x"] == newPos["x"] and currentPos["y"] == newPos["y"]:
			if direction == West:
				direction = North
			elif direction == North:
				direction = East
			elif direction == East:
				direction = South
			elif direction == South:
				direction = West
		else:
			currentPos = tools.get_position()
			
			if direction == West:
				direction = South
			elif direction == North:
				direction = West
			elif direction == East:
				direction = North
			elif direction == South:
				direction = East
		
		if get_entity_type() == Entities.Treasure:
			harvest()
			return 1

def solve_maze_drone(params):
	direction = params["direction"]
	useRightHand = params["rightHand"]
	spawnBudget = params["budget"]
	
	currentPos = tools.get_position()
	maxMoves = parameters.WORLD_SIZE * parameters.WORLD_SIZE * 2
	moveCount = 0
	successiveMovesWithoutWall = 0
	maxSuccessiveMovesWithoutWall = 30
	spawnInterval = 5
	lastSpawn = 0
	spawnRightHand = True
	
	recentPath = []
	pathHistorySize = 6
	
	while get_entity_type() != Entities.Treasure and moveCount < maxMoves:
		if len(recentPath) >= pathHistorySize:
			firstHalf = recentPath[0:3]
			secondHalf = recentPath[3:6]
			match = True
			for i in range(3):
				if firstHalf[i]["x"] != secondHalf[i]["x"] or firstHalf[i]["y"] != secondHalf[i]["y"]:
					match = False
					break
			if match:
				break
		
		moveSuccess = move(direction)
		
		if not moveSuccess:
			if moveCount == 0:
				return
			
			successiveMovesWithoutWall = 0
			
			if useRightHand:
				if direction == West:
					direction = North
				elif direction == North:
					direction = East
				elif direction == East:
					direction = South
				elif direction == South:
					direction = West
			else:
				if direction == West:
					direction = South
				elif direction == South:
					direction = East
				elif direction == East:
					direction = North
				elif direction == North:
					direction = West
		else:
			currentPos = tools.get_position()
			moveCount += 1
			successiveMovesWithoutWall += 1
			
			if len(recentPath) >= pathHistorySize:
				recentPath.pop(0)
			recentPath.append({"x": currentPos["x"], "y": currentPos["y"]})
			
			if successiveMovesWithoutWall >= maxSuccessiveMovesWithoutWall:
				break
			
			if spawnBudget > 0 and moveCount - lastSpawn >= spawnInterval:
				lastSpawn = moveCount
				allDirections = [North, South, East, West]
				
				for spawnDir in allDirections:
					if spawnBudget > 0:
						newParams = {
							"direction": spawnDir,
							"rightHand": spawnRightHand,
							"budget": 0
						}
						spawn_drone(tools.drone_func(solve_maze_drone, newParams))
						spawnBudget -= 1
						spawnRightHand = not spawnRightHand
			
			if useRightHand:
				if direction == West:
					direction = South
				elif direction == North:
					direction = West
				elif direction == East:
					direction = North
				elif direction == South:
					direction = East
			else:
				if direction == West:
					direction = North
				elif direction == North:
					direction = East
				elif direction == East:
					direction = South
				elif direction == South:
					direction = West
	
	if get_entity_type() == Entities.Treasure:
		harvest()

def solve_maze_multi_drone():
	activeDrones = []
	directions = [North, South, East, West]
	
	droneSpawnBudget = 2
	if parameters.DRONE_NUMBER >= 16:
		droneSpawnBudget = 3
	
	for direction in directions:
		paramsRight = {
			"direction": direction,
			"rightHand": True,
			"budget": droneSpawnBudget
		}
		activeDrones.append(spawn_drone(tools.drone_func(solve_maze_drone, paramsRight)))
		
		paramsLeft = {
			"direction": direction,
			"rightHand": False,
			"budget": droneSpawnBudget
		}
		activeDrones.append(spawn_drone(tools.drone_func(solve_maze_drone, paramsLeft)))
	
	for drone in activeDrones:
		wait_for(drone)