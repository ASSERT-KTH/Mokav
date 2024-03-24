def func(*args):
	ret_values = []
	
	number = int(args[0])
	if (number >= 13):
	    ret_values.append(((2 ** number) - (100 * (2 ** (number - 13)))))
	else:
	    ret_values.append((2 ** number))

	return ret_values
