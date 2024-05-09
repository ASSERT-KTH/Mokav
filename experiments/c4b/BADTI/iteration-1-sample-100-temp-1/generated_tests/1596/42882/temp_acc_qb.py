def patched_func(*args):
	global_list = []
	
	s = args[0]
	l = s[0]
	n = 1
	for i in s[1:]:
	    if (i > l):
	        l = i
	        n = 1
	    elif (i == l):
	        n += 1
	global_list.append((l * n))
	return global_list