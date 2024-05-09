def original_func(*args):
	global_list = []
	
	string = args[0]
	(n, a, b) = map(int, string.split())
	if (((a % n) != 0) and ((b % n) != 0)):
	    global_list.append((- 1))
	else:
	    global_list.append(((a // n) + (b // n)))
	return global_list