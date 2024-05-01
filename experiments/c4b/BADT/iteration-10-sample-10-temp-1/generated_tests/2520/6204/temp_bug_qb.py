def original_func(*args):
	global_list = []
	
	x = max(list(map(int, args[0].split())))
	p = ((6 - x) + 1)
	global_list.append(('%d/6' % p))
	return global_list