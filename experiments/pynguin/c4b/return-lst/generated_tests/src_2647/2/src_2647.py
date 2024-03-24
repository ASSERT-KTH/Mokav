def func(*args):
	ret_values = []
	
	n = int(args[0])
	if ((n % 2) == 0):
	    ret_values.append(((n // 2) - 1))
	else:
	    ret_values.append(((n - 1) // 2))

	return ret_values
