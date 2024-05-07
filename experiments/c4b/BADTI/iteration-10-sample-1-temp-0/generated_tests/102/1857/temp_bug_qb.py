def original_func(*args):
	global_list = []
	
	i = sorted(list(map(int, args[0].split())))
	global_list.append(((i[0] + i[1]) * 2))
	return global_list