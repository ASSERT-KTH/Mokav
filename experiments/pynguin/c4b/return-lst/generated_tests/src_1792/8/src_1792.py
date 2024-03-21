def func(*args):
	ret_values = []
	
	n = int(args[0])
	if (n == 2):
	    ret_values.append(3)
	else:
	    ret_values.append((((n ** 3) + (5 * n)) // 6))

	return ret_values
