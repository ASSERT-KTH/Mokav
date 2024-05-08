def original_func(*args):
	global_list = []
	
	n = int(args[0])
	
	def ARG(n):
	    for i in range(2, (n + 1)):
	        if (((n + 1) % i) == 0):
	            return 1
	    return 2
	if (ARG(n) == 2):
	    if (n == 1):
	        global_list.append(3)
	    else:
	        global_list.append(2)
	else:
	    global_list.append(1)
	return global_list