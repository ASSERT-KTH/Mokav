def func(*args):
	ret_values = []
	
	n = int(args[0])
	ret_values.append(((((((n - 1) * n) * (n + 1)) // 6) + n) // 1))

	return ret_values
