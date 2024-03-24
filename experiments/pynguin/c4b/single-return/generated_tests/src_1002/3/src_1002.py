def func(*args):
	
	[n, a, b] = [int(x) for x in args[0].split()]
	return(min((n - a), (b + 1)))
