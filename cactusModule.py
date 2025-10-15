import tools
import farmModule
import parameters

def sort_line(direction):	
	for tries in range(parameters.WORLD_SIZE):
		isSorted = True
		for col in range(parameters.WORLD_SIZE - 1):
			current = measure()
			nextVal = measure(direction)
			
			if current > nextVal:
				isSorted = False
				swap(direction)
			move(direction)
		
		if isSorted:
			return 1
		else:
			move(direction)
	
	move(direction)

def sort_grid():
	tools.drone_grid(sort_line,East)
	tools.go_to(0,0)
	tools.drone_grid(sort_line,North)
	return 1

def execute():
	tools.drone_grid(farmModule.plant_line,Entities.Cactus)
	print("planted")
	tools.go_to(0,0)
	sort_grid()
	print("sorted")
	maxCoord = parameters.WORLD_SIZE - 1
	tools.go_to(maxCoord, maxCoord)
	harvest()

	