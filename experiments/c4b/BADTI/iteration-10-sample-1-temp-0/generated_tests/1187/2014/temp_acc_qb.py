def patched_func(*args):
	global_list = []
	
	s = str(args[0])
	if (s[1:].upper() == s[1:]):
	    global_list.append(s.swapcase())
	else:
	    global_list.append(s)
	return global_list