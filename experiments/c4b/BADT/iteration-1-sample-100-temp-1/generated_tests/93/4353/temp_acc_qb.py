def patched_func(*args):
	global_list = []
	
	(k, a, b) = map(int, args[0].split())
	global_list.append(((((b // k) - (a // k)) - bool((a % k))) + 1))
	return global_list