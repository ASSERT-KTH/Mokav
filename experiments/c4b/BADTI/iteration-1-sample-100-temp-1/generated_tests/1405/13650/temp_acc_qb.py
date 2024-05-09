def patched_func(*args):
	global_list = []
	
	n = int(args[0])
	a = [0, 2, 3, 1, 2, 1]
	global_list.append(a[n])
	return global_list