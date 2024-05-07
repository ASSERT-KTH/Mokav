def original_func(*args):
	global_list = []
	
	s = args[0]
	r = s[1:]
	if (r.isupper() or s.isupper()):
	    global_list.append(s.swapcase())
	else:
	    global_list.append(s)
	return global_list