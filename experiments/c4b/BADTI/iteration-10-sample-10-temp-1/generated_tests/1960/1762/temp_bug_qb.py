def original_func(*args):
	global_list = []
	
	global_list.append(sum(((abs((x - 3)) + abs((y - 3))) for x in range(5) for (y, v) in enumerate(args[0].split()) if int(v))))
	return global_list