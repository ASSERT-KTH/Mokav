def patched_func(*args):
	global_list = []
	
	digits = [8, 4, 2, 6]
	n = int(args[0])
	if (n == 0):
	    global_list.append(1)
	else:
	    global_list.append(digits[((n % 4) - 1)])
	return global_list