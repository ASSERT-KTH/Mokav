def original_func(*args):
	global_list = []
	
	s = args[0]
	n = len(s)
	x = int(s[0])
	global_list.append(((x + 1) * (10 ** (n - 1))))
	return global_list