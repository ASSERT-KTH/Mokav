def original_func(*args):
	global_list = []
	
	import math
	n = int(args[0])
	s = (2 * n)
	t = (math.sqrt((1 + (4 * s))) - 1)
	global_list.append(t)
	if ((t % 2) == 0):
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list