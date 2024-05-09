def original_func(*args):
	global_list = []
	
	digits = [1, 8, 4, 2]
	n = int(args[0])
	if (n < 4):
	    global_list.append(digits[n])
	else:
	    global_list.append(6)
	return global_list