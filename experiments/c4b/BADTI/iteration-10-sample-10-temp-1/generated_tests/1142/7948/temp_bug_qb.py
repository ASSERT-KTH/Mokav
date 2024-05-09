def original_func(*args):
	global_list = []
	
	[n, a, b] = [int(x) for x in args[0].split()]
	global_list.append(min((n - a), ((n + b) // 2)))
	return global_list