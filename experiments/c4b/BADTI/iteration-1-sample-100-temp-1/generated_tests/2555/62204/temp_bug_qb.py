def original_func(*args):
	global_list = []
	
	n = args[0]
	if ((('0' * 7) in n) or (('1' * 7) in n)):
	    global_list.append('yes')
	else:
	    global_list.append('no')
	return global_list