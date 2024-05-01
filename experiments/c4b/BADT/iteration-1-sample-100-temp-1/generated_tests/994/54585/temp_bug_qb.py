def original_func(*args):
	global_list = []
	
	(m, n, a) = map(int, args[0].split())
	times = int((round((m / a), 0) * round((n / a), 0)))
	global_list.append(times)
	return global_list