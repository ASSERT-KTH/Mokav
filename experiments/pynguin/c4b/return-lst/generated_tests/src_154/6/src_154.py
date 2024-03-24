def func(*args):
	ret_values = []
	
	'input\n9 4 3\n'
	(n, a, b) = map(int, args[0].split())
	ret_values.append(min((n - a), (b + 1)))

	return ret_values
