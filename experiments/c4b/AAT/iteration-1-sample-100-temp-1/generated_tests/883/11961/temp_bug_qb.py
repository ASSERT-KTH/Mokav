def original_func(*args):
	global_list = []
	
	s = args[0]
	len({(s[i:] + s[:i]) for i in range(len(s))})
	return global_list