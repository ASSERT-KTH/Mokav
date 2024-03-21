def func(*args):
	ret_values = []
	
	(a, b, c) = map(int, args[0].split())
	ret_values.append(min((2 * min(((a + b), (b + c), (c + a)))), ((a + b) + c)))

	return ret_values
