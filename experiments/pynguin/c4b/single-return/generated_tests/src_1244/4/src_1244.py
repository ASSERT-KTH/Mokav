def func(*args):
	
	I = (lambda : int(args[0]))
	(n, a, b, c) = (I(), I(), I(), I())
	m = max((n // a), ((((n - b) // (b - c)) + 1) if (b <= n) else 0))
	return((m + max(0, (((n - (m * (b - c))) // a) if (b <= n) else 0))))
