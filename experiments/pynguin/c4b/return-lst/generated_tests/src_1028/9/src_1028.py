def func(*args):
	ret_values = []
	
	(x, y, z) = map(int, args[0].split())
	ret_values.append((4 * int((((((x * y) // z) ** 0.5) + (((x * z) // y) ** 0.5)) + (((z * y) // x) ** 0.5)))))

	return ret_values
