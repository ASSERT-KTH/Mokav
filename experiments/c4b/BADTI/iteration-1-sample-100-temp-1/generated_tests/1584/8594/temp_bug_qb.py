def original_func(*args):
	global_list = []
	
	s = args[0]
	while (s.find('//') != (- 1)):
	    s = s.replace('//', '/')
	global_list.append(s)
	return global_list