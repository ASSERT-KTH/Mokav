def patched_func(*args):
	global_list = []
	
	(n, k, l, c, d, p, nl, np) = map(int, args[0].split())
	total_toast = min(((k * l) / nl), (c * d), (p / np))
	global_list.append(int((total_toast / n)))
	return global_list