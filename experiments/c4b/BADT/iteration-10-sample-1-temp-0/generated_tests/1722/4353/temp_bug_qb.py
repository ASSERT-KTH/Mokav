def original_func(*args):
	global_list = []
	
	x = int(args[0])
	k = 0
	i = 1
	while ((i * i) <= x):
	    if ((x % i) == 0):
	        k += bool(set(str(x)).__rand__(set(str(i))))
	    i += 1
	global_list.append((k + bool((x - 1))))
	return global_list