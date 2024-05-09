def original_func(*args):
	global_list = []
	
	n = args[0]
	if (len(n) == 1):
	    global_list.append(n.title())
	elif (n == n.lower()):
	    global_list.append(n)
	else:
	    global_list.append(n.title())
	return global_list