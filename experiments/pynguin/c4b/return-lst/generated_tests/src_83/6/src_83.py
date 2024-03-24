def func(*args):
	ret_values = []
	
	n = int(args[0])
	if ((n % 2) == 0):
	    ret_values.append(((n // 4) - ((n % 4) == 0)))
	else:
	    ret_values.append(0)

	return ret_values
