def func(*args):
	ret_values = []
	
	n = ((int(args[0]) + 1) // 3)
	ret_values.append((n // 12), (n % 12))

	return ret_values
