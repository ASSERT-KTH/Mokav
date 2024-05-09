def original_func(*args):
	global_list = []
	
	s = args[0]
	if s[1:].isupper():
	    if s.isupper():
	        global_list.append(s.lower())
	    else:
	        global_list.append(s.title())
	elif ((len(s) == 1) and s.islower()):
	    global_list.append(s.upper())
	else:
	    global_list.append(s)
	return global_list