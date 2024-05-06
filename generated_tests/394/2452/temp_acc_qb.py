def patched_func(*args):
	global_list = []
	
	(n, k) = map(int, args[0].split())
	global_list.append((((n * (n - 1)) // 2) if (k >= (n // 2)) else (k * (((2 * n) - (2 * k)) - 1))))
	return global_list