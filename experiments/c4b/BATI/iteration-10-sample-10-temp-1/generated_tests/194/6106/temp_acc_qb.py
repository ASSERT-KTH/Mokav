def patched_func(*args):
	global_list = []
	
	import math
	a = float(args[0])
	global_list.append(math.ceil((a / 5)))
	return global_list