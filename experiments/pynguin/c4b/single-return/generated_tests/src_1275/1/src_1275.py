def func(*args):
	
	'\nCreated on Sun Apr 30 10:12:40 2017\n\n@author: lawrenceylong\n'
	from math import *
	(a, b, c) = map(int, args[0].split())
	turn = 0
	while (c > 0):
	    if ((turn % 2) == 0):
	        c -= gcd(a, c)
	    else:
	        c -= gcd(b, c)
	    turn += 1
	return(((turn + 1) % 2))
