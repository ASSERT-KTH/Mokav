def original_func(*args):
	global_list = []
	
	n = int(args[0])
	a = int(args[1])
	b = int(args[2])
	c = int(args[3])
	d = (b - c)
	if ((n < a) and (n < b)):
	    count = 0
	elif (a <= d):
	    count = (n // a)
	else:
	    (count, _) = divmod((n - c), d)
	    count += ((n - (count * d)) // a)
	global_list.append(count)
	return global_list