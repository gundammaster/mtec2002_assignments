"""
exceptions.py
=====
To handle errors, use a try/catch block:

-----
try:
	# do your stuff
except SomeError:
	# deal with some error
-----

optionally... you can continue catching more than one exception:

-----
.
.
except AnotherError:
	# deal with another error
-----

Substitute SomeError with the kind of error you want to handle - for example:

KeyError
ValueError
TypeError
IndexError
ZeroDivisionError
"""
#KeyError
d = {'shape': 'circle'}
try:
	print d['shape']
	print d['color']
except KeyError:
	print "that doesn't exist!!!"
print done
#ValueError (conversion errors)
try:
	print int("this is not a number")
except ValueError:
	print "I don't that's a number"
#TypeError 
try:
	print "foo" * "bar"
except TypeError:
	print"you can't"
#IndexError
my_list = ["some", "stuff"]
try:
	print my_list[2]
except IndexError:
	print"index out of range"
#ZeroDivisionError
try:
	5/0
except ZeroDivisionError:
	print"no-no"
#catching multiple possible exceptions - try possible KeyError AND TypeError like dictionary value divided by another value
#ex... which player do you want to add a score to, and add that score
d = {'score':'10'}
k = 'score'
divisor = 2
try:
	printd[k] / divisor
exceptKeyError:
	print "that doen't exists"
except ZerDivisionError:
	print "you can't divide by 0"