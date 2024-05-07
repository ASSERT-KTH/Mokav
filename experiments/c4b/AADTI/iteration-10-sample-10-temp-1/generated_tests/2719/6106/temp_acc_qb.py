def patched_func(*args):
	global_list = []
	
	(a, b) = map(int, args[0].split(' '))
	i = 0
	while (a <= b):
	    a = (a * 3)
	    b = (b * 2)
	    i = (i + 1)
	global_list.append(i)
	return global_list