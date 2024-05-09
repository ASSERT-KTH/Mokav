def original_func(*args):
	global_list = []
	
	(n, m, z) = map(int, args[0].split())
	global_list.append((z // (n * m)))
	return global_list