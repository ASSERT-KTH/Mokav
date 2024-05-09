def original_func(*args):
	global_list = []
	
	(c1, c2, ll) = [int(x) for x in args[0].split()]
	if ((c1 + c2) < ll):
	    c1 += (c1 + c2)
	else:
	    c1 += ll
	global_list.append((c1 + c2))
	return global_list