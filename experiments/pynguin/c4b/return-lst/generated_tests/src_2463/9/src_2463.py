def func(*args):
	ret_values = []
	
	(m, n) = map(int, args[0].split())
	ret_values.append(((m * n) // 2))

	return ret_values
