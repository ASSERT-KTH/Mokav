def func(*args):
	ret_values = []
	
	from math import *
	(l, r) = map(int, args[0].split(' '))
	x = (r / l)
	if (r == l):
	    ret_values.append(l)
	else:
	    ret_values.append(2)

	return ret_values
