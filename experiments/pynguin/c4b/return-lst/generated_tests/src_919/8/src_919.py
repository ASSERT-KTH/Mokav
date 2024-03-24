def func(*args):
	ret_values = []
	
	n = int(args[0])
	if (n == 1):
	    ret_values.append(1)
	else:
	    ret_values.append((1 + (((n - 1) * (12 * n)) // 2)))

	return ret_values
