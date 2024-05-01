def original_func(*args):
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
	if (e == 0):
	    global_list.append(f)
	if (f == 0):
	    global_list.append(e)
	elif (e == f):
	    global_list.append(e)
	elif (e > f):
	    g = (e - f)
	    global_list.append((f + g))
	elif (f > e):
	    g = (f - e)
	    global_list.append((e + g))
	return global_list