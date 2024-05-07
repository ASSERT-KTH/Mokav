def patched_func(*args):
	global_list = []
	
	a = list(map(int, args[0].split()))
	global_list.append((4 - len(set(a))))
	return global_list