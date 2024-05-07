def patched_func(*args):
	global_list = []
	
	(*l, a, b) = map(int, args[0].split())
	global_list.append(max(0, (min((b + 1), *l) - a)))
	return global_list