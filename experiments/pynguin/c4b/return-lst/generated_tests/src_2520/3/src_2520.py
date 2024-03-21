def func(*args):
	ret_values = []
	
	(m, n) = map(int, args[0].split())
	ret_values.append((((n // 2) * m) + (((n % 2) * m) // 2)))

	return ret_values
