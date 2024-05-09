def original_func(*args):
	global_list = []
	
	n = int(args[0])
	count = 0
	for i in range(1, 6):
	    div = int((n / i))
	    if (div > 0):
	        n -= (div * i)
	        count += div
	    if (n == 0):
	        break
	global_list.append(count)
	return global_list