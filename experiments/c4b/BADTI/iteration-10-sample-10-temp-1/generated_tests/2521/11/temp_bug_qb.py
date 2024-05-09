def original_func(*args):
	global_list = []
	
	import math
	global_list.append(int((math.floor(math.log10(int(args[0]))) + 1)))
	return global_list