def patched_func(*args):
	global_list = []
	
	import math
	(a, b) = map(int, args[0].split())
	global_list.append(int(math.log(((1.5 * b) / a), 1.5)))
	return global_list