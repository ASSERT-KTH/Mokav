def func(*args):
	ret_values = []
	
	(n, k, l, c, d, p, nl, np) = map(int, args[0].split())
	ret_values.append(min(((k * l) // (n * nl)), ((c * d) // n), (p // (np * n))))

	return ret_values
