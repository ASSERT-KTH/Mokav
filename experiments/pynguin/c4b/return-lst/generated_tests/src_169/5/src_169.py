def func(*args):
	ret_values = []
	
	n = int(args[0])
	ret_values.append((((3 ** (3 * n)) - (7 ** n)) % (int(1000000000.0) + 7)))

	return ret_values
