def func(*args):
	ret_values = []
	
	'input\n0\n'
	n = int(args[0])
	ret_values.append(([8, 4, 2, 6][((n % 4) - 1)] if (n != 0) else 1))

	return ret_values
