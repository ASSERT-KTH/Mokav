def patched_func(*args):
	global_list = []
	
	global_list.append((4 - len(set(map(int, args[0].split())))))
	return global_list