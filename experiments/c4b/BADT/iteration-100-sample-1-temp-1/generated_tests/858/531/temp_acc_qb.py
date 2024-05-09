def patched_func(*args):
	global_list = []
	
	'input\n539624191 782710197 514300407 2691939\n'
	(n, a, b, c) = map(int, args[0].split())
	n = (n % 4)
	if (n == 0):
	    global_list.append(0)
	elif (n == 1):
	    global_list.append(min([c, (a + b), (3 * a)]))
	elif (n == 2):
	    global_list.append(min([b, (2 * a), (2 * c)]))
	elif (n == 3):
	    global_list.append(min([a, (b + c), (3 * c)]))
	return global_list