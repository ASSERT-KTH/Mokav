def original_func(*args):
	global_list = []
	
	(l, b) = map(int, args[0].split())
	i = 0
	while (l < b):
	    l *= 3
	    b *= 2
	    i += 1
	global_list.append(i)
	return global_list