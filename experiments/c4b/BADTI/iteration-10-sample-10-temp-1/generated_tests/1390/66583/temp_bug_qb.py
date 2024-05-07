def original_func(*args):
	global_list = []
	
	import math
	a = args[0]
	p = a.split()
	n = float(p[0])
	x = float(p[1])
	y = float(p[2])
	out = math.ceil(((y / 100) * n))
	global_list.append(int((out - x)))
	return global_list