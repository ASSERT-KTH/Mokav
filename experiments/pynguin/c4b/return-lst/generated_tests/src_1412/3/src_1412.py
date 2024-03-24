def func(*args):
	ret_values = []
	
	(a, b, r) = map(int, args[0].split())
	ret_values.append(('Second' if ((a < (2 * r)) or (b < (2 * r))) else 'First'))

	return ret_values
