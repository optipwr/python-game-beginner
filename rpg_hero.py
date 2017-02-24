from Character import Character
import time;
# Give the class a name...Hero
class Hero(object):
	# Call the init method which is built into classes
	# Pass itself so that we have a "this" to work with
	def __init__(self):
		# Define some class properties (attached to self)
    Character.__init__(self);
		self.name = "Michael";
		self.health = 10;
		self.power = 5;
	def alive(self):
		# this returns a boolean value
		return self.health > 0;
	def attack(self, enemy):
		print "%s attacks %s" % (self.name, enemy.name);
		enemy.take_damage(self.power);
		time.sleep(1.5);
		print "%s has done %d damage to %s" % (self.name, self.power, enemy.name)
	def take_damage(self, points_of_damage):
		self.health -= points_of_damage;
	def power_up(self):
		self.power += 5;
		print """%s decides to not attack this turn to contemplate the value of powering up vs attacking as is. %s decides that it is more important to power up this time. %s powers up!""" % (self.name, self.name, self.name);
	def dance(self):
		print "%s drops his weapon and starts dancing. Nothing useful comes from this" % (self.name);
		print """
quu..__
 $$$b  `---.__
  "$$b        `--.                          ___.---uuudP
   `$$b           `.__.------.__     __.---'      $$$$"              .
     "$b          -'            `-.-'            $$$"              .'|
       ".                                       d$"             _.'  |
         `.   /                              ..."             .'     |
           `./                           ..::-'            _.'       |
            /                         .:::-'            .-'         .'
           :                          ::''\          _.'            |
          .' .-.             .-.           `.      .'               |
          : /'$$|           .@"$\           `.   .'              _.-'
         .'|$u$$|          |$$,$$|           |  <            _.-'
         | `:$$:'          :$$$$$:           `.  `.       .-'
         :                  `"--'             |    `-.     .
        :##.       ==             .###.       `.      `.    `.
        |##:                      :###:        |        >     >
        |#'     `..'`..'          `###'        x:      /     /
         \                                   xXX|     /    ./
          \                                xXXX'|    /   ./
          /`-.                                  `.  /   /
         :    `-  ...........,                   | /  .'
         |         ``:::::::'       .            |<    `.
         |             ```          |           x| \ `.:``.
         |                         .'    /'   xXX|  `:`M`M':.
         |    |                    ;    /:' xXXX'|  -'MMMMM:'
         `.  .'                   :    /:'       |-'MMMM.-'
          |  |                   .'   /'        .'MMM.-'
          `'`'                   :  ,'          |MMM<
            |                     `'            |tbap.
             \                                  :MM.-'
              \                 |              .''
               \.               `.            /
                /     .:::::::.. :           /
               |     .:::::::::::`.         /
               |   .:::------------\       /
              /   .''               >::'  /
              `',:                 :    .' """;