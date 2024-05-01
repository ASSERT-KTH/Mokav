def original_func(*args):
	global_list = []
	
	'input\n999999999 1000000000 1000000000 1000000000\n'
	(n, a, b, c) = map(int, args[0].split())
	n = (n % 4)
	if (n == 0):
	    global_list.append(0)
	elif (n == 1):
	    global_list.append(min([c, (a + b), (3 * a)]))
	elif (n == 2):
	    global_list.append(min([b, (2 * a), (2 * c)]))
	elif (n == 3):
	    global_list.append(min([a, (b + c)]))
	return global_list