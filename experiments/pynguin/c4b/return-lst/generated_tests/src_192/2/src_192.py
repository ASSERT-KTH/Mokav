def func(*args):
	ret_values = []
	
	(a, b, c) = sorted(list(map(int, args[0].split())))
	ret_values.append(min(((a + b) << 1), ((a + b) + c)))

	return ret_values
