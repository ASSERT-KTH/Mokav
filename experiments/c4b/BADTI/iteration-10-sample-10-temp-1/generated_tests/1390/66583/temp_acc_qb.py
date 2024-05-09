def patched_func(*args):
	global_list = []
	
	import math
	a = args[0]
	p = a.split()
	n = float(p[0])
	x = float(p[1])
	y = float(p[2])
	out = math.ceil(((y / 100) * n))
	if (int((out - x)) > 0):
	    global_list.append(int((out - x)))
	else:
	    global_list.append(0)
	return global_list