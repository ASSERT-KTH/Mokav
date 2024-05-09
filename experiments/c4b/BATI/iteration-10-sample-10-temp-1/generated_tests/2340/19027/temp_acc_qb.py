def patched_func(*args):
	global_list = []
	
	x = args[0]
	(capital, small, i) = (0, 0, 0)
	while (i < len(x)):
	    if (x[i].isupper() == True):
	        capital += 1
	    else:
	        small += 1
	    i += 1
	if (small >= capital):
	    global_list.append(x.lower())
	else:
	    global_list.append(x.upper())
	return global_list