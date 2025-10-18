import tools
import parameters

def try_moving(direction):
	if not move(direction):
		change_hat(Hats.Brown_Hat)
		return False
	else:
		return True

def finished():
	change_hat(Hats.Brown_Hat)
	return True

def farm_bones():
	change_hat(Hats.Dinosaur_Hat)
	lSize = parameters.WORLD_SIZE - 2
	while True:
		if not try_moving(North):
			return finished()
		direction = East
		for line in range(lSize+1):
			for col in range(lSize):
				if not try_moving(direction):
					return finished()
			if direction == East:
				direction = West
			else:
				direction = East
			if line < lSize and not try_moving(North):
				return finished()

		if not try_moving(East):
			return finished()

		for line in range(lSize+1):
			if not try_moving(South):
				return finished()
		for col in range(lSize+1):
			if not try_moving(West):
				return finished()
		
	change_hat(Hats.Cactus_Hat)

