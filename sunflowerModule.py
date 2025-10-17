import tools
import parameters
import farmModule



def plant_sunflowers():
	allPetals = []
	activeDrones = []
	
	for line in range(parameters.WORLD_SIZE):
		if num_drones() == max_drones():
			petalList = plant_sunflower_line()
			for petalItem in petalList:
				allPetals.append(petalItem)
			continue
		else:	
			while not num_drones() < max_drones(): 
				pass
			activeDrones.append(spawn_drone(plant_sunflower_line))
		move(North)
			
	for drone in activeDrones:
		petalList = wait_for(drone)
		for petalItem in petalList:
			allPetals.append(petalItem)
	return allPetals
	

def plant_sunflower_line():
	petalList = []
	for col in range(parameters.WORLD_SIZE):
		if get_entity_type() != Entities.Sunflower:
			tools.check_till()
			plant(Entities.Sunflower)
			petalNbr = measure()
			if petalNbr > 7:
				petalList.append([get_pos_x(),get_pos_y(),petalNbr])
		move(East)
	return petalList

def harvest_sunflower(petalList):
	activeDrones = []
	
	for i in range(15, 7, -1):
		for drone in activeDrones:
			wait_for(drone)
		for coords in petalList:
			if coords[2] == i:
				if num_drones() == max_drones():
					farmModule.go_to_harvest(coords)
					continue
				else:	
					while not num_drones() < max_drones(): 
						pass
					activeDrones.append(spawn_drone(tools.drone_func(farmModule.go_to_harvest,coords)))

def farm_sunflower():
	tools.go_to(0,0)
	
	petalList = plant_sunflowers()
	
	tools.go_to(0,0)
	while not can_harvest():
		pass
	
	tools.go_to(0,0)
	harvest_sunflower(petalList)

