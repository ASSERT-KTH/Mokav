def patched_func(*args):
	global_list = []
	
	from math import *
	(a, b) = args[0].split()
	(c, d) = args[1].split()
	a = int(a)
	b = int(b)
	c = int(c)
	d = int(d)
	e = abs((a - c))
	f = abs((b - d))
	g = 0
	if (e >= f):
	    global_list.append(e)
	elif (f >= e):
	    global_list.append(f)
	return global_list