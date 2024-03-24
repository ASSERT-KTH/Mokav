def func(*args):
	ret_values = []
	
	e = ((10 ** 9) + 7)
	(a, b, n, x) = map(int, args[0].split())
	t = pow(a, n, (e * max(1, (a - 1))))
	ret_values.append(((((t * x) + ((b * (t - 1)) // (a - 1))) % e) if (a - 1) else ((x + (n * b)) % e)))

	return ret_values
