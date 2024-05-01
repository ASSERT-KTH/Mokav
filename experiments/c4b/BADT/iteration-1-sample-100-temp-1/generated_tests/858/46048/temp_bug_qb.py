def original_func(*args):
	global_list = []
	
	(n, a, b, c) = map(int, args[0].split())
	n = (n % 4)
	if (n == 0):
	    global_list.append(0)
	elif (n == 1):
	    global_list.append(min((3 * a), (a + b), c))
	elif (n == 2):
	    global_list.append(min((2 * a), b, (2 * c)))
	elif (n == 3):
	    global_list.append(min(a, (b + c), (9 * c)))
	return global_list