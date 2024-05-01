def original_func(*args):
	global_list = []
	
	(a, b) = map(int, args[0].strip().split())
	c = 0
	while (a < b):
	    a *= 3
	    b *= 2
	    c += 1
	global_list.append(c)
	return global_list