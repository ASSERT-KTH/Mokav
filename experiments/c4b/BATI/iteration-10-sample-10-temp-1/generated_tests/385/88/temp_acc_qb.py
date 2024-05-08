def patched_func(*args):
	global_list = []
	
	import math
	(h1, h2) = map(int, args[0].split())
	(r, f) = map(int, args[1].split())
	if ((h1 + (r * 8)) >= h2):
	    global_list.append(0)
	elif (f >= r):
	    global_list.append((- 1))
	else:
	    global_list.append(math.ceil((((h2 - h1) - (8 * r)) / (12 * (r - f)))))
	return global_list