def original_func(*args):
	global_list = []
	
	n = args[0]
	n = int(n)
	if (n == 0):
	    global_list.append(1)
	else:
	    a = [0, 8, 4, 2, 6]
	    n = (n % 4)
	    global_list.append(a[n])
	return global_list