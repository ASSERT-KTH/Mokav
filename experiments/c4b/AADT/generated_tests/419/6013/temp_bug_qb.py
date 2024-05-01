def original_func(*args):
	global_list = []
	
	(n, a, b) = map(int, args[0].split(' '))
	if (n == 1):
	    global_list.append(n)
	elif (b > 0):
	    global_list.append(((a + b) % n))
	elif (b < 0):
	    global_list.append(((- (a + b)) % n))
	elif (b == 0):
	    global_list.append(a)
	return global_list