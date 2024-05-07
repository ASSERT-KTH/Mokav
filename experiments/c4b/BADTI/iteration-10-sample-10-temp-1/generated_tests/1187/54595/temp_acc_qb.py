def patched_func(*args):
	global_list = []
	
	s = args[0]
	for i in range(1, len(s)):
	    if (ord(s[i]) > 90):
	        global_list.append(s)
	        exit()
	if (ord(s[0]) > 90):
	    global_list.append((s[0].upper() + s[1:].lower()))
	else:
	    global_list.append(s.lower())
	return global_list