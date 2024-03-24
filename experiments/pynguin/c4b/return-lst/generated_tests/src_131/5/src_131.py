def func(*args):
	ret_values = []
	
	'input\n12\n'
	n = int(args[0])
	if ((n % 5) == 0):
	    ret_values.append((n // 5))
	else:
	    ret_values.append(((n // 5) + 1))

	return ret_values
