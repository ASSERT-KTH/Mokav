def func(*args):
	ret_values = []
	
	(d1, d2, d3) = map(int, args[0].split())
	ret_values.append(((min(d1, d2) + min((d1 + d2), d3)) + min(max(d1, d2), (d3 + min(d1, d2)))))

	return ret_values
