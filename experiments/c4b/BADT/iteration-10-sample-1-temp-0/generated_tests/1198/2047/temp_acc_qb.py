def patched_func(*args):
	global_list = []
	
	x = args[0]
	i = 0
	z = 'NO'
	for i in range(len(x)):
	    if ((x[i] == 'H') or (x[i] == 'Q') or (x[i] == '9')):
	        z = 'YES'
	    i += 1
	global_list.append(z)
	return global_list