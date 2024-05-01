def original_func(*args):
	global_list = []
	
	a = int(args[0])
	ans = int((3 ** (((a ** 2) - a) / 2)))
	global_list.append(ans)
	return global_list