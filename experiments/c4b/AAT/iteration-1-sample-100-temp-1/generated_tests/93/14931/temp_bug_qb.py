def original_func(*args):
	global_list = []
	
	(k, a, b) = map(int, args[0].split())
	if ((a % k) and (b % k)):
	    global_list.append(((b - a) // k))
	else:
	    global_list.append((1 + ((b - a) // k)))
	return global_list