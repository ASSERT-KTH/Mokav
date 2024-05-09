def original_func(*args):
	global_list = []
	
	s = args[0]
	s = s.title()
	global_list.append(s)
	return global_list