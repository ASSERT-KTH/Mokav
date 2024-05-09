def patched_func(*args):
	global_list = []
	
	import math
	n = int(args[0])
	global_list.append([(math.ceil((n / 4)) - 1), 0][((n % 2) != 0)])
	return global_list