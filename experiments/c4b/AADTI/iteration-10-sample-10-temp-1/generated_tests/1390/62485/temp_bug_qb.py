def original_func(*args):
	global_list = []
	
	import math
	data = args[0].split()
	(N, X, Y) = (int(data[0]), int(data[1]), int(data[2]))
	global_list.append((math.ceil((N * (Y / 100))) - X))
	return global_list