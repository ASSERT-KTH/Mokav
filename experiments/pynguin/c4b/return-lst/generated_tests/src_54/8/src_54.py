def func(*args):
	ret_values = []
	
	(x, y, z) = map(int, args[0].split())
	ret_values.append(min(((x + y) + z), (2 * (x + y)), (2 * (y + z)), (2 * (x + z))))

	return ret_values
