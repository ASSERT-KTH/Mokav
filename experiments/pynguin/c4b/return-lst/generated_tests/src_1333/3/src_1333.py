def func(*args):
	ret_values = []
	
	(a, b) = map(int, args[0].split())
	ret_values.append((((a + b) - 1) - min(a, b)), min(a, b))

	return ret_values
