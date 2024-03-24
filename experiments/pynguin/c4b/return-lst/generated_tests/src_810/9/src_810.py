def func(*args):
	ret_values = []
	
	(n, a, b) = map(int, args[0].split())
	ret_values.append(((n - max((a + 1), (n - b))) + 1))

	return ret_values
