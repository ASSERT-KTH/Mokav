def func(*args):
	
	(n, a, b) = [int(i) for i in args[0].split()]
	return(min((n - a), (b + 1)))
