import tools
import parameters


def try_moving(direction):
	if not move(direction):
		change_hat(Hats.Brown_Hat)
		return False
	else:
		return True

def farm_bones():
	change_hat(Hats.Dinosaur_Hat)
	lSize = parameters.WORLD_SIZE - 2
	finished = False
	while not finished:
		if not try_moving(North):
			finished = True
			break
		direction = East
		for line in range(lSize+1):
			for col in range(lSize):
				if not try_moving(direction):
					finished = True
					break
			if direction == East:
				direction = West
			else:
				direction = East
			if line < lSize and not try_moving(North):
				finished = True
				break

		if not try_moving(East):
			finished = True
			break

		for line in range(lSize+1):
			if not try_moving(South):
				finished = True
				break
		for col in range(lSize+1):
			if not try_moving(West):
				finished = True
				break
		
	change_hat(Hats.Cactus_Hat)
				
			
				


	
