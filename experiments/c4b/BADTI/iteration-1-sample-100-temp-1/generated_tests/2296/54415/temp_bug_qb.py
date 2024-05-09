def original_func(*args):
	global_list = []
	
	import sys
	(n, m) = map(float, args[0].split())
	global_list.append(round(((n * m) / 2)))
	return global_list