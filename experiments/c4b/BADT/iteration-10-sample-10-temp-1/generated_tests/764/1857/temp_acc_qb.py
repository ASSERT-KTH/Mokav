def patched_func(*args):
	global_list = []
	
	i = list(map(int, args[0].split()))
	global_list.append((max(i) - min(i)))
	return global_list