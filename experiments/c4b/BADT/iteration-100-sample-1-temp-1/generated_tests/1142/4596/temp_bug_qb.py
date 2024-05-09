def original_func(*args):
	global_list = []
	
	data = [int(x) for x in args[0].split()]
	p = (data[0] - data[1])
	pf = ((data[0] - p) - data[2])
	if (pf <= 0):
	    pf = 0
	global_list.append((p - pf))
	return global_list