def original_func(*args):
	global_list = []
	
	s = args[0]
	if (s.isupper() or ((s[0].lower() and s[1:].isupper()) if (len(s) > 1) else True)):
	    global_list.append((s[0].upper() + s[1:].lower()))
	else:
	    global_list.append(s)
	return global_list