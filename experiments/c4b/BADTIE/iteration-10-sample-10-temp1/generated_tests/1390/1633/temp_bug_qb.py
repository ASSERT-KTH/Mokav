def original_func(*args):
	global_list = []
	
	import math
	string = args[0]
	(n, x, y) = map(int, string.split())
	global_list.append((math.ceil(((y / 100) * n)) - x))
	return global_list