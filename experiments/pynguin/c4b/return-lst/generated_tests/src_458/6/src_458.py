def func(*args):
	ret_values = []
	
	n = int(args[0])
	ret_values.append((sum((((i + 1) * ((n - i) - 1)) for i in range(n))) + n))

	return ret_values
