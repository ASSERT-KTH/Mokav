def func(*args):
	ret_values = []
	
	import math
	a = args[0]
	p = a.split()
	n = float(p[0])
	x = float(p[1])
	y = float(p[2])
	out = math.ceil(((y / 100) * n))
	if (int((out - x)) > 0):
	    ret_values.append(int((out - x)))
	else:
	    ret_values.append(0)

	return ret_values
