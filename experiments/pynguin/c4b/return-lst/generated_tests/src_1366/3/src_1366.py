def func(*args):
	ret_values = []
	
	number = int(args[0])
	n = int(((1 + ((1 + (8 * (number - 1))) ** (1 / 2))) / 2))
	ret_values.append((number - ((n * (n - 1)) // 2)))

	return ret_values
