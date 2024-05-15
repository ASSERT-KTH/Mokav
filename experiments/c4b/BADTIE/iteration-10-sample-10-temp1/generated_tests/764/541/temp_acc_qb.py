def patched_func(*args):
	global_list = []
	
	l = list(map(int, args[0].split()))
	l.sort()
	global_list.append((l[2] - l[0]))
	return global_list