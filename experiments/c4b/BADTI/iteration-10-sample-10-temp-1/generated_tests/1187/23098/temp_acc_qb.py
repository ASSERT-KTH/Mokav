def patched_func(*args):
	global_list = []
	
	n = args[0]
	if (n[1:] == n[1:].upper()):
	    if (n[0] == n[0].upper()):
	        global_list.append(n.lower())
	    else:
	        global_list.append((n[0].upper() + n[1:].lower()))
	else:
	    global_list.append(n)
	return global_list