def original_func(*args):
	global_list = []
	
	s = args[0]
	if (s[0].islower() or s[1:].isupper()):
	    global_list.append(s.capitalize())
	elif s.isupper():
	    global_list.append(s.lower())
	else:
	    global_list.append(s)
	return global_list