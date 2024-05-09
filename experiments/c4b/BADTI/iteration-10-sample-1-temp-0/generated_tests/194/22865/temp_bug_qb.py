def original_func(*args):
	global_list = []
	
	n = int(args[0])
	m = n
	x = 0
	while (m > 5):
	    x = (m // 5)
	    m = 0
	    global_list.append((x + 1))
	if (n <= 5):
	    global_list.append('1')
	return global_list