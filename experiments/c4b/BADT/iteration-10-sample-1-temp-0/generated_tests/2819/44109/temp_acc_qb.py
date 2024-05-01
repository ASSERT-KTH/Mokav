def patched_func(*args):
	global_list = []
	
	from math import *
	(l, r) = map(int, args[0].split(' '))
	x = (r / l)
	if (r == l):
	    global_list.append(l)
	else:
	    global_list.append(2)
	return global_list