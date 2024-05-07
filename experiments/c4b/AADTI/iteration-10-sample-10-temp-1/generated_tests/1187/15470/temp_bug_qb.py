def original_func(*args):
	global_list = []
	
	s = args[0]
	if (s[0].islower() and s[1:].isupper()):
	    global_list.append((s[0].upper() + s[1:].lower()))
	elif s.isupper():
	    global_list.append(s.lower())
	else:
	    global_list.append(s)
	return global_list