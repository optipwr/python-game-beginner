class Zombie(object):
	def __init__(self,speed,strength,hunger,weapon,health):
		self.speed = speed;
		self.strength = strength;
		self.hunger = hunger;
		self.weapon = weapon;
		self.health = health;
		self.type = 'zombie';

# print vars(zombie_object);
# print dir(zombie_object);