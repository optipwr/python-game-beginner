class Animal(object):
	def __init__(self, name):
		self.name = name;

	def speak(self):
		print self.name + " is gurgling uncontrollably";

	def run(self):
		print self.name + " is running away from the bullets";

animal1 = Animal("Mitzee");
animal1.speak();
animal1.run();

# make a new class instead of passing "object" we pass the name of the parent class!
class Dog(Animal):
	def __init__(self, dog_name):
		Animal.__init__(self, dog_name);
		print self.name;
	def bark(self):
		print self.name + " is trying to bark, but can't breathe!";

dog = Dog("Fieldor");
dog.bark();
