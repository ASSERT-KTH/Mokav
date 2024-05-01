def patched_func(*args):
	global_list = []
	
	a = [int(x) for x in args[0].split()]
	global_list.append(int(((a[0] * a[1]) / 2)))
	return global_list