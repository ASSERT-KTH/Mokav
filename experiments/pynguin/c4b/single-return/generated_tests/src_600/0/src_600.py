def func(*args):
	
	(n, k) = map(int, args[0].split())
	return((((n * (n - 1)) // 2) if (k >= (n // 2)) else (k * (((2 * n) - (2 * k)) - 1))))
