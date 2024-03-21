def func(*args):
	ret_values = []
	
	(d1, d2, d3) = [int(i) for i in args[0].split()]
	res = min(((d1 + d2) + d3), ((d1 * 2) + (d2 * 2)), ((d1 * 2) + (d3 * 2)), ((d2 * 2) + (d3 * 2)))
	ret_values.append(res)

	return ret_values
