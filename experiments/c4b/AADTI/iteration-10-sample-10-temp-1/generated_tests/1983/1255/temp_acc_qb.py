def patched_func(*args):
	global_list = []
	
	n = int(args[0])
	m = 0
	p = 2
	if (n == 1):
	    global_list.append(1)
	elif (n == 2):
	    global_list.append(3)
	elif (n > 2):
	    for i in range((n - 2), 0, (- 1)):
	        m += ((i * p) + 1)
	        p += 1
	    global_list.append(((n + m) + 1))
	return global_list