def original_func(*args):
	global_list = []
	
	import math
	a = int(args[0])
	b = int(math.sqrt(a))
	if ((b * (b + 1)) == a):
	    global_list.append('NO')
	else:
	    global_list.append('YES')
	return global_list