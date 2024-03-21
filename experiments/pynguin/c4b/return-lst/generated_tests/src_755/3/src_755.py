def func(*args):
	ret_values = []
	
	n = int(args[0])
	ret_values.append(((((n + 3) // 4) - 1) * ((n % 2) == 0)))

	return ret_values
