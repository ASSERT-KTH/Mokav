def patched_func(*args):
	global_list = []
	
	import math
	(h1, h2) = map(int, args[0].split())
	(a, b) = map(int, args[1].split())
	if ((h1 + (a * 8)) >= h2):
	    global_list.append(0)
	elif (b >= a):
	    global_list.append((- 1))
	else:
	    global_list.append(math.ceil((((h2 - h1) - (8 * a)) / (12 * (a - b)))))
	return global_list