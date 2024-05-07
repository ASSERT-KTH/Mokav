def original_func(*args):
	global_list = []
	
	x = args[0]
	y = '1111111'
	z = '0000000'
	if ((y in x) or (z in x)):
	    global_list.append('yes')
	else:
	    global_list.append('No')
	return global_list