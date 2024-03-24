def func(*args):
	ret_values = []
	
	n = int(args[0])
	if ((n % 2) == 0):
	    ret_values.append(int((((n / 2) - 1) / 2)))
	else:
	    ret_values.append('0')

	return ret_values
