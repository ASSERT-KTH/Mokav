def func(*args):
	ret_values = []
	
	a = int(args[0])
	if (a >= 13):
	    ret_values.append(((2 ** a) - (100 * (2 ** (a - 13)))))
	else:
	    ret_values.append((2 ** a))

	return ret_values
