def patched_func(*args):
	global_list = []
	
	(n, m, a) = map(int, args[0].split())
	global_list.append((((n // a) + ((n % a) > 0)) * ((m // a) + ((m % a) > 0))))
	return global_list