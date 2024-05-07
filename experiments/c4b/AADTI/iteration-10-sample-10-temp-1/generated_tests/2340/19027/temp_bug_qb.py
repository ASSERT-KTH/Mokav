def original_func(*args):
	global_list = []
	
	x = args[0]
	(capital, small) = (0, 0)
	if (x[0].isupper() == True):
	    capital += 1
	else:
	    small += 1
	if (small > capital):
	    global_list.append(x.lower())
	else:
	    global_list.append(x.upper())
	return global_list