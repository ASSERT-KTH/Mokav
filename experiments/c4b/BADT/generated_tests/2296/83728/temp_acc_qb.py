def patched_func(*args):
	global_list = []
	
	from math import floor
	[a, b] = map(int, args[0].split())
	global_list.append(floor(((a * b) * (1 / 2))))
	return global_list