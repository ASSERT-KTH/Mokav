def patched_func(*args):
	global_list = []
	
	import math
	(a, b, c) = map(int, args[0].split(' '))
	global_list.append(max(math.ceil((((a * c) / 100) - b)), 0))
	return global_list