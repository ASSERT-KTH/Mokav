def patched_func(*args):
	global_list = []
	
	x = int(args[0])
	y = ((x + 4) // 5)
	global_list.append(y)
	return global_list