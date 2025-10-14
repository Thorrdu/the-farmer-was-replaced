import tools
import mazeModule
import cactusModule
import bonesModule
import sunflowerModule
import parameters

def farm_crop(cropType):
	tools.go_to(0,0)
	
	if cropType == Entities.Grass:
		tools.drone_grid(farm_line, cropType)
	elif cropType == Entities.Sunflower:
		sunflowerModule.farm_sunflower()
	elif cropType in [Entities.Tree, Entities.Carrot]:
		if get_entity_type() != cropType:
			tools.drone_grid(plant_line, cropType)
		tools.drone_grid(farm_line, cropType)
	elif cropType == Entities.Pumpkin:
		if get_entity_type() != cropType:
			tools.drone_grid(plant_line, cropType)
		harvest()
	elif cropType == Entities.Cactus:
		cactusModule.execute()
	elif cropType == Items.Bone:
		bonesModule.farm_bones()
	elif cropType == Items.Gold:
		mazeModule.farm_treasures()
	else:
		print("KESKEJEFAI?????")

def farm_line(cropType):
	for col in range(parameters.WORLD_SIZE):	
		currentCrop = get_entity_type()
				
		if can_harvest():
			harvest()
	
		if currentCrop != Entities.Grass:
			plant_crop(currentCrop)
			
		move(East)	
	return 1

def plant_line(cropType):
	for col in range(parameters.WORLD_SIZE):
		
		if cropType == Entities.Tree:
			if get_pos_y() % 2 == 0 and col % 2 == 0:
				plant_crop(cropType)
			elif get_pos_y() % 2 == 0 :
				plant_crop(Entities.Bush)
			elif get_pos_y() % 2 != 0 and col % 2 != 0:
				plant_crop(Entities.Tree)
			else:
				plant_crop(Entities.Bush)
		else:
			plant_crop(cropType)
		move(East)
	return 1

def plant_crop(cropType):
	if cropType != Entities.Grass:
		tools.check_till()
		while get_water() < 0.5:
			use_item(Items.Water)
			
		if cropType == Entities.Pumpkin:
			plant(cropType)
			use_item(Items.Fertilizer)

			while not can_harvest():
				if get_entity_type() == Entities.Dead_Pumpkin:
					plant_crop(cropType)				
		else:
			plant(cropType)
		
	return 1
