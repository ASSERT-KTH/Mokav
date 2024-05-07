def patched_func(*args):
	global_list = []
	
	i = sorted(list(map(int, args[0].split())))
	global_list.append(min(((i[0] + i[1]) * 2), ((i[0] + i[2]) + i[1])))
	return global_list