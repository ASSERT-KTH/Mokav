def patched_func(*args):
	global_list = []
	
	a = args[0]
	b = list(a)
	if (len(b) == 1):
	    if (a == a.upper()):
	        global_list.append(a.lower())
	    else:
	        global_list.append(a.upper())
	elif (a.lower() == a):
	    global_list.append(a)
	elif (a.upper() == a):
	    global_list.append(a.lower())
	elif (b[0].lower() == b[0]):
	    c = a[1:]
	    if (c.upper() == c):
	        global_list.append((b[0].upper() + c.lower()))
	    else:
	        global_list.append(a)
	elif (b[0].upper() == b[0]):
	    global_list.append(a)
	return global_list