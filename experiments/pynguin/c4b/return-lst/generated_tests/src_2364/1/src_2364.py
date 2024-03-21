def func(*args):
	ret_values = []
	
	(n, k, l, c, d, p, nl, np) = map(int, args[0].split())
	total_toast = min(((k * l) / nl), (c * d), (p / np))
	ret_values.append(int((total_toast / n)))

	return ret_values
