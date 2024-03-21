def func(*args):
	ret_values = []
	
	(a, b, c) = map(int, args[0].split())
	ret_values.append(min(((a + b) + c), ((2 * a) + (2 * c)), ((2 * b) + (2 * c)), ((2 * a) + (2 * b))))

	return ret_values
