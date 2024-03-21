def func(*args):
	ret_values = []
	
	(n, a, b, c) = map(int, args[0].split())
	ret_values.append([0, min((3 * a), (a + b), c), min((2 * a), b, (2 * c)), min(a, (b + c), (3 * c))][(n % 4)])

	return ret_values
