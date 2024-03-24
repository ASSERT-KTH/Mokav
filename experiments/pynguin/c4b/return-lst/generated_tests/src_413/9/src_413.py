def func(*args):
	ret_values = []
	
	n = int(args[0])
	ret_values.append((((n // 2) - 1) + (n % 2)))

	return ret_values
