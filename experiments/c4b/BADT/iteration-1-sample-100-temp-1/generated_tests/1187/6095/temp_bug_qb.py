def original_func(*args):
	global_list = []
	
	x = args[0]
	if (x.isupper() or (x[0].islower() and x[1:len(x)].isupper())):
	    x = x.swapcase()
	global_list.append(x)
	return global_list