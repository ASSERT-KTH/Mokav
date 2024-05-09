def original_func(*args):
	global_list = []
	
	s = args[0]
	l = 8
	h = 0
	if ((s[0] == '1') or (s[0] == '8')):
	    h = 1
	    l -= 3
	if ((s[1] == 'a') or (s[1] == 'h')):
	    if (h == 1):
	        l -= 2
	    else:
	        l -= 3
	global_list.append(l)
	return global_list