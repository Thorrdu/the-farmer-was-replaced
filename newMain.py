import tools
import farmModule
import parameters

clear()

if parameters.WORLD_SIZE < get_world_size():
	set_world_size(parameters.WORLD_SIZE)

currentCrop = None
lastCrop = currentCrop

firstLoop = True
while True:
	currentCrop = tools.priority_crop()
	
	if lastCrop != currentCrop and not firstLoop:
		tools.smart_clear()
	
	lastCrop = currentCrop
	farmModule.farm_crop(currentCrop)
	
	firstLoop = False
	
