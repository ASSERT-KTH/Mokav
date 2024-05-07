def patched_func(*args):
	global_list = []
	
	from math import ceil
	n = int(args[0])
	global_list.append(ceil(max(0, ((n / 2) - 1))))
	return global_list