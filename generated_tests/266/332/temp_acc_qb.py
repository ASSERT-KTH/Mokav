def patched_func(*args):
	global_list = []
	
	n = int(args[0])
	m = (((((((n - 4) * (n - 3)) * (n - 2)) * (n - 1)) * n) ** 2) // 120)
	global_list.append(m)
	return global_list