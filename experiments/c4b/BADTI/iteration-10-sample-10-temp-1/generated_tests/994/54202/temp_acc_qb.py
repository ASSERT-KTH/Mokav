def patched_func(*args):
	global_list = []
	
	from math import ceil
	(n, m, a) = map(int, args[0].split())
	global_list.append((ceil((n / a)) * ceil((m / a))))
	return global_list