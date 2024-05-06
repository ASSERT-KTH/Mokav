def original_func(*args):
	global_list = []
	
	n = int(args[0])
	for i in range(210, (n + 1)):
	    if ((n % i) == 0):
	        while ((n % (i ** 2)) != 0):
	            global_list.append(i)
	return global_list