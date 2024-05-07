def original_func(*args):
	global_list = []
	
	n1 = args[0].split()
	n = int(n1[0])
	k = int(n1[1])
	if (k >= (n // 2)):
	    global_list.append(((n * (n - 1)) // 2))
	else:
	    global_list.append((((k * k) + ((2 * k) * (n - (2 * k)))) + k))
	return global_list