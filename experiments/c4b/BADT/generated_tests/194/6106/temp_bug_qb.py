def original_func(*args):
	global_list = []
	
	import math
	a = int(args[0])
	global_list.append(math.ceil(a))
	return global_list