def original_func(*args):
	global_list = []
	
	x = args[0]
	if ((len(x) < 2) or x[1:].isupper()):
	    x = (x[0].upper() + x[1:].lower())
	global_list.append(x)
	return global_list