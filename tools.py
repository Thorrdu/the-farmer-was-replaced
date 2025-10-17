import parameters

worldSize = parameters.WORLD_SIZE
farmCycleCounter = 0

def is_even(n):
	return n % 2 == 0

def check_till():
	if get_ground_type() != Grounds.Soil:
		till()
	return True

def priority_crop():
	global farmCycleCounter
	
	if parameters.PRIORITY_CROP != None:
		return parameters.PRIORITY_CROP
	
	farmCycleCounter += 1
	
	if farmCycleCounter % parameters.SUNFLOWER_CYCLE == 0:
		return Entities.Sunflower
	
	bestCrop = None
	lowestScore = 999999
	
	for plant in parameters.PLANTS:
		if plant["plant"] == Entities.Sunflower:
			continue
		
		currentAmount = num_items(plant["item"])
		targetAmount = plant["target"]
		plantPriority = plant["priority"]
		
		if targetAmount > 0:
			progressRatio = currentAmount / targetAmount
		else:
			progressRatio = 0
		
		score = progressRatio / plantPriority
		
		if score < lowestScore:
			lowestScore = score
			bestCrop = plant["plant"]
	
	if bestCrop != None:
		return bestCrop
	else:
		return Entities.Grass


def get_position():
	return({"x":get_pos_x(), "y":get_pos_y()})

def harvest_line(crop):
	for col in range(worldSize):
		if can_harvest():
			harvest()
		move(East)
	return 1

def smart_clear():
	drone_grid(harvest_line, None)
	go_to(0,0)
	clear()

def go_to(x, y):
	currentPos = get_position()
	currentX = currentPos["x"]
	currentY = currentPos["y"]
	
	diffX = x - currentX
	if abs(diffX) > worldSize/2:
		if diffX > 0:
			diffX = -1 * (worldSize - abs(diffX))
		else:
			diffX = (worldSize - abs(diffX))
	
	diffY = y - currentY
	if abs(diffY) > worldSize/2:
		if diffY > 0:
			diffY = -1 * (worldSize - abs(diffY))
		else:
			diffY = (worldSize - abs(diffY))
	
	if diffX > 0:
		direction = East
	else:
		direction = West
	for _ in range(abs(diffX)):
		move(direction)
	
	if diffY > 0:
		direction = North
	else:
		direction = South
	for _ in range(abs(diffY)):
		move(direction)

def drone_func(f, arg):
	def g():
		f(arg)
	return g
	
def call_func(f, arg):
	def g():
		f(arg)
	g()
	
def drone_grid(function,parameter):
	go_to(0,0)
	maxDrones = parameters.DRONE_NUMBER - 1
	farmedLines = 0
	activeDrones = []
	while True:
		
		if farmedLines == worldSize:
			break

		while farmedLines < worldSize and num_drones() < max_drones():
			activeDrones.append(spawn_drone(drone_func(function,parameter)))
			farmedLines += 1
			if parameter != North:
				move(North)
			else:
				move(East)
				
		if farmedLines < worldSize and num_drones() == max_drones():
			call_func(function,parameter)
			farmedLines += 1
		
			if parameter != North:
				move(North)
			else:
				move(East)
			
		for drone in activeDrones:
			wait_for(drone)
			
def combine(arrayA, arrayB):
	for itemB in arrayB:
		arrayA.append(arrayB)
	return arrayA	
		