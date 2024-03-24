def func(*args):
	ret_values = []
	
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
	    ret_values.append(e)
	elif (f >= e):
	    ret_values.append(f)

	return ret_values
