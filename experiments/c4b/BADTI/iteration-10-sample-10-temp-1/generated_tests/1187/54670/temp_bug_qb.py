def original_func(*args):
	global_list = []
	
	n = args[0]
	n_1 = n[1:]
	if (n.isupper() == True):
	    global_list.append(n.lower())
	elif ((n_1.isupper() == True) and (n[:1].islower() == True)):
	    global_list.append(n.capitalize())
	else:
	    global_list.append(n)
	return global_list