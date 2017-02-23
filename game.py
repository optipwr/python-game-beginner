from zombie import Zombie
import hero

# Make a zombie object from the class
zombie_object = Zombie(6,8,19,'bat',15);

print vars(zombie_object);

# Make a hero object from the hero class
hero_object = hero.Hero();
# hero.cheer_hero(hero_object);
hero_object.cheer_hero();