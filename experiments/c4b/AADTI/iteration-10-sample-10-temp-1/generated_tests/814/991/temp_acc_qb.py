def patched_func(*args):
	global_list = []
	
	(k, r) = map(int, args[0].split())
	i = 1
	while (((((i * k) - r) % 10) != 0) and (((i * k) % 10) != 0)):
	    i += 1
	global_list.append(i)
	return global_list