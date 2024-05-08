def original_func(*args):
	global_list = []
	
	import math
	(a, b) = (int(args[0]), int(args[1]))
	n = math.log(b, a)
	if (int(n) == n):
	    global_list.append('YES')
	    global_list.append((int(n) - 1))
	else:
	    global_list.append('NO')
	return global_list