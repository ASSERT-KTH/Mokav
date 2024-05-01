def patched_func(*args):
	global_list = []
	
	import math
	string = args[0]
	(n, x, y) = map(int, string.split())
	a = math.ceil(((y / 100) * n))
	if (a < x):
	    global_list.append(0)
	else:
	    global_list.append((a - x))
	return global_list