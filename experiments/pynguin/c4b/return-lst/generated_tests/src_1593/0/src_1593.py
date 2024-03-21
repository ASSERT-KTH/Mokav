def func(*args):
	ret_values = []
	
	(a, b) = map(int, args[0].split())
	ret_values.append(((a * b) // 2))

	return ret_values
