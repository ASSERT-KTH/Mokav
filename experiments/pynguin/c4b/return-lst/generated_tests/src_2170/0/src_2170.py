def func(*args):
	ret_values = []
	
	n = int(args[0])
	ret_values.append((pow(3, (n - 1), 1000003) if n else 1))

	return ret_values
