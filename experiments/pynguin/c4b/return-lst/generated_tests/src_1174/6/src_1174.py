def func(*args):
	ret_values = []
	
	(n, k) = map(int, args[0].split())
	ret_values.append(max(((3 * n) - k), 0))

	return ret_values
