def func(*args):
	
	(n, a, b) = map(int, args[0].split())
	return(((n - a) if ((n - a) <= (b + 1)) else (b + 1)))
