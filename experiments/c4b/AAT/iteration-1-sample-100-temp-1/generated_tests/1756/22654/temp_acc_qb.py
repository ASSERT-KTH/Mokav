def patched_func(*args):
	global_list = []
	
	n = set(map(int, args[0].split()))
	global_list.append((4 - len(n)))
	return global_list