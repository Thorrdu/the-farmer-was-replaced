import tools
import parameters

def plant_sunflower_line(cropType):
	for col in range(parameters.WORLD_SIZE):
		if get_entity_type() != Entities.Sunflower:
			tools.check_till()
			plant(Entities.Sunflower)
		move(East)
	return 1

def measure_sunflower_line(cropType):
	petalList = []
	for col in range(parameters.WORLD_SIZE):
		if get_entity_type() == Entities.Sunflower:
			petals = measure()
			if petals != None:
				currentPos = tools.get_position()
				petalList.append({"petals": petals, "x": currentPos["x"], "y": currentPos["y"]})
		move(East)
	return petalList

def harvest_single_sunflower(coords):
	tools.go_to(coords["x"], coords["y"])
	if can_harvest():
		harvest()

def farm_sunflower():
	tools.go_to(0,0)
	
	tools.drone_grid(plant_sunflower_line, Entities.Sunflower)
	
	tools.go_to(0,0)
	while not can_harvest():
		pass
	
	tools.go_to(0,0)
	allPetals = []
	for line in range(parameters.WORLD_SIZE):
		petalsInLine = measure_sunflower_line(None)
		for petal in petalsInLine:
			allPetals.append(petal)
		move(North)
	
	if len(allPetals) > 0:
		maxPetals = 0
		for sunflowerData in allPetals:
			if sunflowerData["petals"] > maxPetals:
				maxPetals = sunflowerData["petals"]
		
		while maxPetals > 0:
			sunflowersAtThisLevel = []
			for sunflowerData in allPetals:
				if sunflowerData["petals"] == maxPetals:
					sunflowersAtThisLevel.append(sunflowerData)
			
			maxDronesPerBatch = parameters.DRONE_NUMBER - 1
			harvestedCount = 0
			totalToHarvest = len(sunflowersAtThisLevel)
			
			while harvestedCount < totalToHarvest:
				activeDrones = []
				dronesInThisBatch = 0
				
				while dronesInThisBatch < maxDronesPerBatch and harvestedCount < totalToHarvest:
					sunflowerCoords = sunflowersAtThisLevel[harvestedCount]
					activeDrones.append(spawn_drone(tools.drone_func(harvest_single_sunflower, sunflowerCoords)))
					dronesInThisBatch += 1
					harvestedCount += 1
				
				for drone in activeDrones:
					wait_for(drone)
			
			maxPetals -= 1
	
	tools.go_to(0,0)

