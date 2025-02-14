# Basic concepts in  classes with Python
# the self stands for the current instance of the class object that we are reffering to
# the class is like a blueprint for a project
class Dog:
	def __init__(self, name):
		self.name = name

	def bark(self):
		print(f"{self.name} says woof!")

# creating objects from the class
my_dog = Dog("Anxiel")
my_dog.bark()

