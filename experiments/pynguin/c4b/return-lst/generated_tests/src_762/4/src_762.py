def func(*args):
	ret_values = []
	
	f = (lambda x, y: (f((y % x), x) if x else y))
	(a, b, x, y) = map(int, args[0].split())
	z = f(x, y)
	x //= z
	y //= z
	m = min((a // x), (b // y))
	ret_values.append((m * x), (m * y))

	return ret_values
