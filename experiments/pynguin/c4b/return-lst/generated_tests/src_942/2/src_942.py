def func(*args):
	ret_values = []
	
	(n, a, b) = map(int, str(args[0]).strip().split())
	ret_values.append(((n - max((a + 1), (n - b), 1)) + 1))

	return ret_values
