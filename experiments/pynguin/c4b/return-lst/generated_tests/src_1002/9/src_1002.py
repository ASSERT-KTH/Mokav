def func(*args):
	ret_values = []
	
	[n, a, b] = [int(x) for x in args[0].split()]
	ret_values.append(min((n - a), (b + 1)))

	return ret_values
