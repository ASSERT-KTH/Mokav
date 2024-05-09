def original_func(*args):
	global_list = []
	
	import math
	n = list(map(int, args[0].split()))
	global_list.append((math.ceil(((n[0] * n[2]) / 100)) - n[1]))
	return global_list