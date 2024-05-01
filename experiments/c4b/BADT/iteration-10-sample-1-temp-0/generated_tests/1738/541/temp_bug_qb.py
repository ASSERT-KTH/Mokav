def original_func(*args):
	global_list = []
	
	import math
	(v1, v2, v3) = map(int, args[0].split())
	global_list.append(int((4 * ((math.sqrt(((v1 * v2) / v3)) + math.sqrt(((v2 * v3) / v1))) + math.sqrt(((v1 * v3) / v3))))))
	return global_list