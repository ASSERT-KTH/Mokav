def patched_func(*args):
	global_list = []
	
	from math import ceil
	(n, m, a) = [int(x) for x in args[0].split(' ')]
	global_list.append((ceil((n / a)) * ceil((m / a))))
	return global_list