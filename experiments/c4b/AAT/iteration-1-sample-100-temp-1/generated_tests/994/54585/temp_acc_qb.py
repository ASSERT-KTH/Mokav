def patched_func(*args):
	global_list = []
	
	from math import ceil
	(m, n, a) = map(int, args[0].split())
	times = (ceil((m / a)) * ceil((n / a)))
	global_list.append(times)
	return global_list