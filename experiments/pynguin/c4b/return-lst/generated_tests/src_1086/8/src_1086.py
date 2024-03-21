def func(*args):
	ret_values = []
	
	n = int(args[0])
	ret_values.append(((((n // 2) - 1) // 2) if ((n != 1) and ((n % 2) == 0)) else 0))

	return ret_values
