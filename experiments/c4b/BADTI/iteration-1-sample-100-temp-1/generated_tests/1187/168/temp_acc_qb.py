def patched_func(*args):
	global_list = []
	
	n = args[0]
	if (len(n) == 1):
	    if n.isupper():
	        global_list.append(n.lower())
	    else:
	        global_list.append(n.upper())
	    exit(0)
	if n.isupper():
	    global_list.append(n.lower())
	elif (n[0].islower() and n[1:].isupper()):
	    global_list.append((n[0].upper() + n[1:].lower()))
	else:
	    global_list.append(n)
	return global_list