def original_func(*args):
	global_list = []
	
	import math
	(n, x, y) = map(int, args[0].split(' '))
	global_list.append(math.ceil((((y * n) / 100) - x)))
	return global_list