def func(*args):
	
	(n, k) = map(int, args[0].split())
	return((((n // k) + 1) * k))
