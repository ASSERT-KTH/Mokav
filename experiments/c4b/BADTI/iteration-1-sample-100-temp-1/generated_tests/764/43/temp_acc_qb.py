def patched_func(*args):
	global_list = []
	
	line = sorted([int(x) for x in args[0].split(' ')])
	global_list.append(str((line[2] - line[0])))
	return global_list