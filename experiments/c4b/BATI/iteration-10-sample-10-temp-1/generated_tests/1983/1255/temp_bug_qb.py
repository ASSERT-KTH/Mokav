def original_func(*args):
	global_list = []
	
	n = int(args[0])
	m = 0
	p = 2
	for i in range((n - 2), 0, (- 1)):
	    m += ((i * p) + 1)
	    global_list.append(i, p)
	    p += 1
	    global_list.append(((n + m) + 1))
	return global_list