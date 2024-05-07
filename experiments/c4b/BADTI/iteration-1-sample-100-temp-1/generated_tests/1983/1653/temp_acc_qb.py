def patched_func(*args):
	global_list = []
	
	n = int(args[0])
	c = 0
	for i in range(1, (n + 1)):
	    if (i == 1):
	        c += n
	    elif (i == n):
	        c += 1
	    else:
	        c += (((i - 1) * ((n + 1) - i)) + 1)
	global_list.append(c)
	return global_list