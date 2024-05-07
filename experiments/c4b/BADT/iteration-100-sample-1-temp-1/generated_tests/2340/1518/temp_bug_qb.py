def original_func(*args):
	global_list = []
	
	a = args[0]
	l = 0
	u = 0
	for i in a:
	    if i.islower():
	        l += 1
	    else:
	        u += 1
	if (l > u):
	    global_list.append(a.upper())
	else:
	    global_list.append(a.lower())
	return global_list