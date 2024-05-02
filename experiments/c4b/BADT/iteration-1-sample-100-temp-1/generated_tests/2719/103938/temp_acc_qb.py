def patched_func(*args):
	global_list = []
	
	(a, b) = map(int, args[0].split())
	i = 0
	while (a <= b):
	    a *= 3
	    b *= 2
	    i += 1
	global_list.append(i)
	return global_list