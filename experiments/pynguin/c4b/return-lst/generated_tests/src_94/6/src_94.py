def func(*args):
	ret_values = []
	
	(n, k, m) = map(int, args[0].split())
	ret_values.append(((n - max((k + 1), (n - m))) + 1))

	return ret_values
