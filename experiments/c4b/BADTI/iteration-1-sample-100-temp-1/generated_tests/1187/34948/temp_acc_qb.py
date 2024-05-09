def patched_func(*args):
	global_list = []
	
	s = args[0]
	if (len(s) == 1):
	    s = s.swapcase()
	else:
	    if (s[0].islower() and s[1:].isupper()):
	        s = s.swapcase()
	    if s.isupper():
	        s = s.swapcase()
	global_list.append(s)
	return global_list