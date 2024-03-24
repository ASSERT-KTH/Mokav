def func(*args):
	ret_values = []
	
	n = int(args[0])
	ret_values.append(((1 << (n + 1)) - 2))

	return ret_values
