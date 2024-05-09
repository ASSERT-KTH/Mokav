def original_func(*args):
	global_list = []
	
	s = str(args[0])
	if s[0].islower():
	    global_list.append(s.swapcase())
	else:
	    global_list.append(s)
	return global_list