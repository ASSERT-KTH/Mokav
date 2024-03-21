def func(*args):
	ret_values = []
	
	n = int(args[0])
	ret_values.append(int(((n * ((n ** 2) + 5)) / 6)))

	return ret_values
