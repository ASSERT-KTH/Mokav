def func(*args):
	ret_values = []
	
	(a, b, c) = map(int, args[0].split())
	k = (((a * b) * c) ** 0.5)
	ret_values.append((4 * int((((k / a) + (k / b)) + (k / c)))))

	return ret_values
