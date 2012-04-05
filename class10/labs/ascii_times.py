"""
ascii_times.py
=====
1. create a dictionary of ascii art - {"heart":"<3", "person":">-|o"}
2. loop forever
3. ask for a key
4. ask for the number of times the ascii art should be printed
5. print out the ascii art that number of times
6. what happens if we input a non-numeric value for number of times
7. what happens if we input a key that doesn't exist?
"""
d = {"heart":"<3", "person":">-|o", "tree": "----o"}
while True:
	print "gimmeh key"
	key = raw_input('>')
	print "gimmeh number of times"
	num = raw_input('>')
	try:
		print d[key] * int(num)
	except KeyError:
		print "key doesn't exist"
	except ValueError:
		print ""