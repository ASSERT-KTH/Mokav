def func(*args):
	ret_values = []
	
	n = int(args[0])
	ret_values.append(((n // 2) if ((n % 2) == 1) else ((n // 2) - 1)))

	return ret_values
