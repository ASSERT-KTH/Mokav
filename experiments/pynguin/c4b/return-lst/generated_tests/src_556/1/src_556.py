def func(*args):
	ret_values = []
	
	(x, y, z) = map(int, args[0].split())
	ret_values.append(min((x - y), (z + 1)))

	return ret_values
