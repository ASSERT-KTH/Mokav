def func(*args):
	ret_values = []
	
	digits = [8, 4, 2, 6]
	n = int(args[0])
	if (n == 0):
	    ret_values.append(1)
	else:
	    ret_values.append(digits[((n % 4) - 1)])

	return ret_values
