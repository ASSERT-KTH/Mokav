def func(*args):
	ret_values = []
	
	n = int(args[0])
	ret_values.append(((((((n ** 2) * ((n - 1) ** 2)) * ((n - 2) ** 2)) * ((n - 3) ** 2)) * ((n - 4) ** 2)) // ((((1 * 2) * 3) * 4) * 5)))

	return ret_values
