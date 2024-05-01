def patched_func(*args):
	global_list = []
	
	s = args[0]
	if ((not s[1:]) or s[1:].isupper()):
	    if s[0].islower():
	        global_list.append((s[0].upper() + s[1:].lower()))
	    else:
	        global_list.append((s[0].lower() + s[1:].lower()))
	else:
	    global_list.append(s)
	return global_list