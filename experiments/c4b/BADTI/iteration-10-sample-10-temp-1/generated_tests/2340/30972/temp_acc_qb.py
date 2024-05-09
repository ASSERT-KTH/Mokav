def patched_func(*args):
	global_list = []
	
	str = args[0]
	n_lower = 0
	n_upper = 0
	for c in str:
	    if c.islower():
	        n_lower += 1
	    elif c.isupper():
	        n_upper += 1
	if (n_upper > n_lower):
	    global_list.append(str.upper())
	else:
	    global_list.append(str.lower())
	return global_list