def func(*args):
	
	(n, m, a) = map(int, args[0].split())
	return(((((n + a) - 1) // a) * (((m + a) - 1) // a)))
