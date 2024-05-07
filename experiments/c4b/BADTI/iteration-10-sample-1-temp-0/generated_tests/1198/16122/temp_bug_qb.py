def original_func(*args):
	global_list = []
	
	a = list(args[0])
	if (('H' in a) or ('Q' in a) or ('9' in a)):
	    global_list.append('Yes')
	else:
	    global_list.append('No')
	return global_list