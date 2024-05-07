def patched_func(*args):
	global_list = []
	
	d = {1: 2, 2: 3, 3: 1, 4: 2, 5: 1}
	global_list.append(d[int(args[0])])
	return global_list