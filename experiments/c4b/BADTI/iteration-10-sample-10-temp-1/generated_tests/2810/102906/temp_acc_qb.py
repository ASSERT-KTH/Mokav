def patched_func(*args):
	global_list = []
	
	import math
	n = int(args[0])
	global_list.append((math.ceil((n / 2)) - 1))
	return global_list