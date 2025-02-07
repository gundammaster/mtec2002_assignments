"""
point.py
=====
We'll make a class that represents a new data type - a point in the
x, y plain.  We'll create some attributes and methods for this class.

This exercise was derived from:

http://www.openbookproject.net/thinkcs/python/english2e/ch13.html

Some information about classes:
1. self refers to the instance of the class
2. underscore methods have meaning
3. __init__(self) is a constructor
4. __str__ should return the desired string representation of the instance

We'll define 5 methods:
====
__init__(self, x, y):
__str__(self):
reset_to_origin(self):
distance_from_origin(self):
distance_from(self, p):

Example usage of the Point class:

p = Point(-2,1)
print p.distance_from(Point(1,5))
print p.distance_from_origin()
p.reset_to_origin()
print p

Expected Output:
=====
5.0
2.23606797749979
(0,0)


"""
import math

# we want to create our own data type - we already have strings, lists, etc
class point:
	def __init__(self,x,y):
		self.x = x
		self. y = y
	def __str__(self):
		return "(%s,%s)" % (self.x,self.y)
	def distance_from(self, p):
		d = math.sqrt(math.pow(p.x - self.x,2) + math.pow(p.y - self.y,2))
		return
	def reset_to_origin(self,x,y):
		self.x = 0
		self.y = 0
		#return "(%s,%s)" % (self.x,self.y)
a = point (5,10)
print a
print a.x
print a.y
b = point (-1,-5)
print b

# there are special methods that you can define in each class
# add a constructor, __init__, so that the point is forced to be initialized to some value
# try creating a point without passing parameters, run your program
# remove the previous, and instead, try creating a point with initial parameters
# try printing the point object, run your program

# create a distance_from function that takes another point and calculates distance 
# distance formula:  http://en.wikipedia.org/wiki/Distance#Geometry
# use the method on the following points  -2, 1 and 1, 5, run your program
# import the math module to use the sqrt and pow functions

# put in docstrings for the class and the methods - you can see them in the interactive shell

# on your own - write another method that sets self.x and self.y to 0 and call it reset_to_origin
# outside of the class, try using the function on an instance of this class
# print out the result

# (INTERMEDIATE) implement a distance_from_origin function that takes no arguments, but instead calculate the distance of the instance point to the origin
# hint: you can call a method within your class using self. you can also pass a Point object as a parameter to a method.
