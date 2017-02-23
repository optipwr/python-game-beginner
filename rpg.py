from rpg_hero import Hero;

from rpg_monsters import Goblin;

hero = Hero();
enemies = [Goblin()];

for enemy in enemies:
	# Loop through all the bad guys in the enemies list
	print vars(enemy);
	# while hero.health > 0 and enemy.health > 0:
	while hero.alive() and enemy.alive():
		print "What will you do?";
		print "1. Fight %s" % enemy.name;
		print "2. Run Away";
		print "3. Power up";
		print "4. Dance";
		print "> ",
		input = int(raw_input());
		if input == 1:
			# user has chosen to fight!
			# subtract health from enemy = hero power
			hero.attack(enemy);
		elif input == 2:
			# User has chosen to run away. break out of the while loop
			break;
		elif input == 3:
			hero.power_up();
		elif input == 4:
			hero.dance();
		else:
			print "Invalid choice. You idiot, you chose: %r which isn't an option!" % input;
		if enemy.alive():
			# user has made their choice and now it's the enemies turn
			# if the enemy has health
			# hero.health -= enemy.power;
			enemy.attack(hero);
	if hero.alive():
		# We know they won, because someones health is <= 0
		print "You won! The %s is defeated!" % enemy.name;
	else:
		# We know the hero lost
		print "You were defeated by the violent %s" % enemy.name;
		