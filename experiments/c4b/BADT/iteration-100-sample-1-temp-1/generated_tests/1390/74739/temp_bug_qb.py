def original_func(*args):
	global_list = []
	
	import math
	(n, k, p) = map(int, args[0].split())
	need = math.ceil(((n * p) / 100))
	global_list.append((need - k))
	return global_list