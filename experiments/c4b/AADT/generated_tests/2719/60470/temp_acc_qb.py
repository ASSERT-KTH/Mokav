def patched_func(*args):
	global_list = []
	
	(a, b) = map(int, args[0].split())
	x = 0
	while (a <= b):
	    x += 1
	    a *= 3
	    b *= 2
	global_list.append(x)
	return global_list