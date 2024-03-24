def func(*args):
	ret_values = []
	
	(n, k) = map(int, args[0].split())
	ret_values.append((((n // k) + 1) * k))

	return ret_values
