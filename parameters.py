WORLD_SIZE = get_world_size()
PRIORITY_CROP = Items.Gold
DRONE_NUMBER = max_drones()

PLANTS = [
	{
		"name":"sunflower",
		"plant":Entities.Sunflower,
		"item":Items.Power,
		"target":100000,
		"priority":10
	},
	{
		"name":"hay",
		"plant":Entities.Grass,
		"item":Items.Hay,
		"target":10000000000,
		"priority":5
	},
	{
		"name":"tree",
		"plant":Entities.Tree,
		"item":Items.Wood,
		"target":100000000000,
		"priority":5
	},
	{
		"name":"carrot",
		"plant":Entities.Carrot,
		"item":Items.Carrot,
		"target":10000000000,
		"priority":5
	},
	{
		"name":"pumpkin",
		"plant":Entities.Pumpkin,
		"item":Items.Pumpkin,
		"target":1000000,
		"priority":4
	},
	{
		"name":"cactus",
		"plant":Entities.Cactus,
		"item":Items.Cactus,
		"target":10000000000,
		"priority":4
	},
	{
		"name":"bones",
		"plant":Items.Bone,
		"item":Items.Bone,
		"target":100000000,
		"priority":3
	},
	{
		"name":"gold",
		"plant":Items.Gold,
		"item":Items.Gold,
		"target":100000000,
		"priority":3
	},

]

SUNFLOWER_CYCLE = 10


def get_plant(value,index):
	for plant in PLANTS:
		if plant[index] == value:
			return plant
