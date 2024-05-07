def original_func(*args):
	global_list = []
	
	import math
	(h1, h2) = map(int, args[0].split())
	diffe = (h2 - h1)
	(a, b) = map(int, args[1].split())
	if ((h1 + (a * 8)) >= h2):
	    global_list.append(0)
	elif (a > b):
	    global_list.append(math.ceil(((((h2 - h1) - (8 * a)) / 12) * (a - b))))
	else:
	    global_list.append((- 1))
	return global_list