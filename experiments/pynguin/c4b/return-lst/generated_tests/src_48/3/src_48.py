def func(*args):
	ret_values = []
	
	(x, y) = map(int, args[0].split())
	ret_values.append(int((int(((x / y) + 1)) * y)))

	return ret_values
