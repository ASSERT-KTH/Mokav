def func(*args):
	ret_values = []
	
	(d1, d2, d3) = map(int, args[0].split())
	ret_values.append(min(((d1 + d2) + d3), ((d1 * 2) + (d2 * 2)), ((d1 * 2) + (d3 * 2)), ((d2 * 2) + (d3 * 2))))

	return ret_values
