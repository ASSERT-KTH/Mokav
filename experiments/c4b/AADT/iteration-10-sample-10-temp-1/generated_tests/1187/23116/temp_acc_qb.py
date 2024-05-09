def patched_func(*args):
	global_list = []
	
	s = args[0]
	if (s[0].islower() and s[1:].isupper()):
	    global_list.append(s.capitalize())
	elif s.isupper():
	    global_list.append(s.lower())
	elif ((len(s) == 1) and s.islower()):
	    global_list.append(s.upper())
	else:
	    global_list.append(s)
	return global_list