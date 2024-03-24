def func(*args):
	ret_values = []
	
	'input\n100 33 34\n'
	(d1, d2, d3) = map(int, args[0].split())
	ret_values.append(min(((2 * d1) + (2 * d2)), ((d1 + d2) + d3), ((2 * d1) + (2 * d3)), ((2 * d2) + (2 * d3))))

	return ret_values
