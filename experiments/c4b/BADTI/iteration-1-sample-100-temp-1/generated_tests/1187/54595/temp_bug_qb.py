def original_func(*args):
	global_list = []
	
	s = args[0]
	for i in range(1, len(s)):
	    if (ord(s[i]) > 90):
	        global_list.append(s)
	        exit()
	global_list.append((s[0].upper() + s[1:].lower()))
	return global_list