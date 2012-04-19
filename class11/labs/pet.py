"""
pet.py
=====
Create a class called Pet, subclass it to create a Dog and Cat class

Pet will have a speak and speak_twice method, as well as a name attribute that is initialized in a constructor.

Example Output:
>>> p = pet.Pet("mojo")
>>> print p
mojo
>>> p.speak()
generic animal talk
>>> p.speak_twice()
generic animal talk
generic animal talk
>>> c = pet.Cat("mittens")
>>> print c
mittens
>>> c.speak_twice()
meow
meow
>>> 
"""
class pet:
	def __init__ (self,n):
		self.name = n
	def __str__(self):
		return self.name
	def procreate(self,p):
		return pet("baby")
	def speak(self):
		print "animal sound"
	def speak_twice(self):
		self.speak()
		self.speak()
class dog(pet):
	def speak(self):
		print "woof"
p = pet("fluffy")
print p
d = dog("spot")
print d
d.speak