def func(*args):
	
	(n, a, b) = map(int, args[0].split())
	return(min((n - a), (b + 1)))
