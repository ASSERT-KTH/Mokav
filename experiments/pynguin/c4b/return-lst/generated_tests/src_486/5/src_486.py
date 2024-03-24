def func(*args):
	ret_values = []
	
	(n, a, b) = (int(i) for i in args[0].split())
	ret_values.append(min((n - a), (b + 1)))

	return ret_values
