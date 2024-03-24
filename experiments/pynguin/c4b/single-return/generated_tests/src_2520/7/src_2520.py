def func(*args):
	
	(m, n) = map(int, args[0].split())
	return((((n // 2) * m) + (((n % 2) * m) // 2)))
