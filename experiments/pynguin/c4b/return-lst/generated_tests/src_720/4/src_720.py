def func(*args):
	ret_values = []
	
	(n, a, b) = map(int, args[0].split())
	ret_values.append(min((b + 1), (n - a)))

	return ret_values
