def patched_func(*args):
	global_list = []
	
	global_list.append(sum(((abs((x - 2)) + abs((y - 2))) for x in range(5) for (y, v) in enumerate(args[0].split()) if int(v))))
	return global_list