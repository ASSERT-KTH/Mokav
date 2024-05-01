def original_func(*args):
	global_list = []
	
	'\nCreated on Sun Apr 30 10:12:40 2017\n\n@author: lawrenceylong\n'
	from math import *
	(a, b, c) = map(int, args[0].split())
	turn = 0
	while (c > 0):
	    if ((turn % 2) == 0):
	        c -= gcd(a, c)
	    else:
	        c -= gcd(b, c)
	global_list.append((turn % 2))
	return global_list