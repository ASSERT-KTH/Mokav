def patched_func(*args):
	global_list = []
	
	(n, a, b, c) = args[0].split()
	n = int(n)
	resto = (4 - (n % 4))
	if (resto == 4):
	    global_list.append(0)
	elif (resto == 1):
	    global_list.append(min([int(a), (int(b) + int(c)), (int(c) * 3)]))
	elif (resto == 2):
	    global_list.append(min([(int(a) * 2), int(b), (int(c) * 2)]))
	else:
	    global_list.append(str(min([(int(a) * 3), (int(a) + int(b)), int(c)])))
	return global_list