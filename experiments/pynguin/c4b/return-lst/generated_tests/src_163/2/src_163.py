def func(*args):
	ret_values = []
	
	'input\n3\n'
	n = int(args[0])
	if (n < 3):
	    ret_values.append((- 1))
	else:
	    ret_values.append(((((10 ** (n - 1)) // 210) + 1) * 210))

	return ret_values
