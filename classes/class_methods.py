# In this  file we will look at the different methods to declare the methods in the class
#class Example:
#	def instance_method(self, arg1, arg2):
#		print(f"Instance method with {arg1} and {arg2}")
#
#obj = Example()
#obj.instance_method("Artificial", "Intelligence")

# The second way
# class Example:
#	@classmethod
#	def class_method(cls, arg1, arg2):
#		print(f"class method with {arg1} and {arg2}")
#
#Example.class_method("Artificial", "Inteligence")

#The third way {The static method }
#class Example:
#	@staticmethod
#	def static_method(arg1, arg2):
#		print(f"Staticmethod with {arg1} and {arg2}")
#
#Example.static_method("Artificial", "Intelligence")

# this method will show the 3 methods used together in the same place
class Student:
	school_name = "Python High"

	def __init__(self, name):
		self.name = name

# in this instance, self  is needed
	def  get_student_info(self, nam):
		return f"Student: {self.name}"

# In this case class is required
	@classmethod
	def get_school_info(cls):
		return f"School: {cls.school_name}"

# static method, needs neither class nor self
	@staticmethod
	def get_school_hours():
		return f"School hours: 8AM - 3 PM"

# Using the different methods
student = Student("Anxiel")

# Method requiring an instance
print(student.get_student_info("Anxiel"))

# Method requiring the class
print(Student.get_school_info())
print(student.get_school_info())

# Static methods can be called on instances or classes
print(Student.get_school_hours())
print(student.get_school_hours())


