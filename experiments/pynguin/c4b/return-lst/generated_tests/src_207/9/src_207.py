def func(*args):
	ret_values = []
	
	(n, m) = map(int, args[0].split())
	ret_values.append(((n * m) // 2))

	return ret_values
