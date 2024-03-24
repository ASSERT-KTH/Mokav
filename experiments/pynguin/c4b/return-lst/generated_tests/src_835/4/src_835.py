def func(*args):
	ret_values = []
	
	(n, a, b) = map(int, args[0].split())
	ret_values.append(((n - a) if ((n - a) <= (b + 1)) else (b + 1)))

	return ret_values
