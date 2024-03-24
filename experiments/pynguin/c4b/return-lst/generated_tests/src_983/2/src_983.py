def func(*args):
	ret_values = []
	
	(n, m, a) = map(int, args[0].split())
	ret_values.append(((((n + a) - 1) // a) * (((m + a) - 1) // a)))

	return ret_values
