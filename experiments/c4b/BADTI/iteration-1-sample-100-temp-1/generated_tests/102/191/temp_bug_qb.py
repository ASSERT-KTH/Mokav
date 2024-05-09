def original_func(*args):
	global_list = []
	
	(a, b, c) = map(int, args[0].split())
	sum1 = ((a * 2) + (b * 2))
	sum2 = ((a + b) + c)
	if (sum1 < sum2):
	    global_list.append(sum1)
	else:
	    global_list.append(sum2)
	return global_list