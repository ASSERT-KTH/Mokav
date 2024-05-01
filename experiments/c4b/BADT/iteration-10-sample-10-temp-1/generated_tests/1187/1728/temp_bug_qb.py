def original_func(*args):
	global_list = []
	
	x = args[0]
	if (x.isupper() or x[1:].isupper()):
	    x = x.lower()
	global_list.append(x)
	return global_list