def patched_func(*args):
	global_list = []
	
	n = int(args[0])
	if ((n % 2) == 1):
	    global_list.append(('7' + ('1' * ((n - 3) // 2))))
	else:
	    global_list.append(('1' * (n // 2)))
	return global_list