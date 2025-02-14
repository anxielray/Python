# Basic concepts in  classes with Python
# the self stands for the current instance of the class object that we are reffering to
# the class is like a blueprint for a project
class Dog:
	def __init__(self, name):
		self.name = name

	def bark(self):
		print(f"{self.name} says woof!")

# creating objects from the class
# Attributes are the variable that belong to the class
# Methods are functions that belong to the same class
# A special constructor(method) that runcswhrn the new object is created
my_dog = Dog("Anxiel")
my_dog.bark()

