def func(*args):
	ret_values = []
	
	n = int(args[0])
	ret_values.append((((((n ** 2) + n) // 2) * 6) + 1))

	return ret_values
