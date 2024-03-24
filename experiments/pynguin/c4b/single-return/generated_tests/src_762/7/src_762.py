def func(*args):
	
	f = (lambda x, y: (f((y % x), x) if x else y))
	(a, b, x, y) = map(int, args[0].split())
	z = f(x, y)
	x //= z
	y //= z
	m = min((a // x), (b // y))
	return((m * x), (m * y))
