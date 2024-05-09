def original_func(*args):
	global_list = []
	
	n = args[0]
	if (('1111111' in n) or ('0000000' in n)):
	    global_list.append('yes')
	else:
	    global_list.append('no')
	return global_list