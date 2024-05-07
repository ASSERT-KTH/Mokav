def patched_func(*args):
	global_list = []
	
	n = int(args[0])
	
	def ARG(n):
	    for i in range(2, (n + 1)):
	        if (((n + 1) % i) == 0):
	            return 1
	    return 2
	k = 1
	p = (n * k)
	while (ARG(p) == 2):
	    k = (k + 1)
	    p = (n * k)
	global_list.append(k)
	return global_list