def original_func(*args):
	global_list = []
	
	str = args[0]
	n_lower = 0
	n_upper = 0
	for c in str:
	    if c.islower():
	        n_lower += 1
	    elif c.isupper():
	        n_upper += 1
	if (n_lower > n_upper):
	    global_list.append(str.lower())
	else:
	    global_list.append(str.upper())
	return global_list