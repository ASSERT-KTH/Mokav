def func(*args):
	ret_values = []
	
	(n, m) = map(int, args[0].split())
	ret_values.append(((pow(3, n, m) - 1) % m))

	return ret_values
