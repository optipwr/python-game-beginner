from Character import Character
class Goblin(Character):
	def __init__(self):
		Character.__init__(self);
		self.name = "goblin";
		self.health = 6;
		self.power = 22;
	def alive(self):
		# this returns a boolean value
		return self.health > 0;
	def take_damage(self, points_of_damage):
		self.health -= points_of_damage;
	def attack(self, hero):
		print "%s attacks %s" % (self.name, hero.name);
		hero.take_damage(self.power);