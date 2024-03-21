def func(*args):
	ret_values = []
	
	(x1, x2, x3) = map(int, args[0].split())
	ret_values.append((max(x1, x2, x3) - min(x1, x2, x3)))

	return ret_values
