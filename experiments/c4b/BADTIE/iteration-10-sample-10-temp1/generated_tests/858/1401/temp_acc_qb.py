def patched_func(*args):
	global_list = []
	
	(n, a, b, c) = map(int, args[0].split())
	mod = (n % 4)
	if (mod == 0):
	    global_list.append(0)
	elif (mod == 1):
	    global_list.append(min((3 * a), c, (a + b)))
	elif (mod == 2):
	    global_list.append(min((2 * a), b, (2 * c)))
	elif (mod == 3):
	    global_list.append(min(a, (3 * c), (b + c)))
	return global_list