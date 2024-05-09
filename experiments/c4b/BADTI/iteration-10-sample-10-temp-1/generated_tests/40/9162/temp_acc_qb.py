def patched_func(*args):
	global_list = []
	
	n = int(args[0])
	for i in range(2, (10 ** 6)):
	    while ((n % (i ** 2)) == 0):
	        n = (n // i)
	global_list.append(n)
	return global_list