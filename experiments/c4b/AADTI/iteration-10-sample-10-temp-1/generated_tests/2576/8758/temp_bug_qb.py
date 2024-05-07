def original_func(*args):
	global_list = []
	
	temp = args[0]
	(k, a, b) = map(int, temp.split(' '))
	if ((a < k) and (b < k)):
	    global_list.append((- 1))
	else:
	    global_list.append(((a // k) + (b // k)))
	return global_list