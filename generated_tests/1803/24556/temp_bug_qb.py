def original_func(*args):
	global_list = []
	
	n = int(args[0])
	if (n <= 2):
	    global_list.append(n)
	elif ((n % 2) == 0):
	    global_list.append(max((((n * (n - 1)) * (n - 2)) // 2), (((n - 1) * (n - 2)) * (n - 3)), ((n * (n - 1)) * (n - 3))))
	else:
	    global_list.append(((n * (n - 1)) * (n - 2)))
	return global_list