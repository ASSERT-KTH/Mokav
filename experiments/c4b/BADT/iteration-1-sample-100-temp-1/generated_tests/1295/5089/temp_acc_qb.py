def patched_func(*args):
	global_list = []
	
	(n, k, l, c, d, p, nl, np) = map(int, args[0].split())
	global_list.append(min(((k * l) // (n * nl)), ((c * d) // n), (p // (np * n))))
	return global_list