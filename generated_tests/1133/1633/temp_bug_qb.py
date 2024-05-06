def original_func(*args):
	global_list = []
	
	s = args[0]
	if ('4' in s):
	    global_list.append(4)
	elif ('7' in s):
	    global_list.append(7)
	else:
	    global_list.append((- 1))
	return global_list