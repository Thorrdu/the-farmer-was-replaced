import tools

def is_even(n):
	return n % 2 == 0
	
def is_carrot(n,u):
	return (n / u) * 100 < 65

wSize = get_world_size()	

clear()
tools.go_to(0,0)
canTill = True
while True:

	for i in range(wSize):
		for j in range(wSize):
			linePercent = (i / wSize) * 100
			if can_harvest():
				harvest()

			if canTill and (linePercent > 30 or i == 1 or i == 4):
				till()	
				
			if i == 1:
				plant(Entities.Carrot)
			elif i == 4:
				plant(Entities.Sunflower)
			elif is_even(i) == True and linePercent <= 30:
				if is_even(j) == True:
					plant(Entities.Tree)
				else:
					plant(Entities.Bush)
			elif linePercent <= 30:
				#herbe
				move(East)
				continue
			elif is_carrot(i,wSize-1):
				plant(Entities.Carrot)
			else:
				use_item(Items.Water)
				use_item(Items.Water)
				plant(Entities.Pumpkin)
				use_item(Items.Fertilizer)
				
				while can_harvest() != True:
					plant(Entities.Pumpkin)
			move(East)
		move(North)
	canTill = False