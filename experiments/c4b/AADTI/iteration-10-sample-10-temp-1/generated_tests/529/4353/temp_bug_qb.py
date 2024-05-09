def original_func(*args):
	global_list = []
	
	e = ((10 ** 9) + 7)
	(a, b, n, x) = map(int, args[0].split())
	t = pow(a, n, (e * max(1, (a - 1))))
	global_list.append(((((t * x) + ((b * (t - 1)) // (a - 1))) % e) if (a - 1) else ((a * x) + b)))
	return global_list