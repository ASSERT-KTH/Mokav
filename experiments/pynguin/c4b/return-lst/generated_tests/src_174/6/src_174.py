def func(*args):
	ret_values = []
	
	n = int(args[0])
	b = (n // 2)
	if (n < 3):
	    ret_values.append((- 1))
	elif ((n % 2) == 1):
	    ret_values.append(((2 * b) * (b + 1)), (((2 * b) * (b + 1)) + 1))
	else:
	    ret_values.append(((b * b) - 1), ((b * b) + 1))

	return ret_values
