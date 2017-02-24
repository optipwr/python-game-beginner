class Character(object):
	# def __init__(self):
	def take_damage(self, points_of_damage):
		self.health -= points_of_damage;
	def attack(self, hero):
		print "%s attacks %s" % (self.name, hero.name);
		hero.take_damage(self.power);