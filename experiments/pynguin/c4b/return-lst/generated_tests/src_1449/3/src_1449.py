def func(*args):
	ret_values = []
	
	n = int(args[0])
	ret_values.append(((n // 5) if ((n % 5) == 0) else ((n // 5) + 1)))

	return ret_values
