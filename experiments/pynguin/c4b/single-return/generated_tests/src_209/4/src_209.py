def func(*args):
	
	(n, a, b, c) = [int(args[0]) for i in range(4)]
	g = max(0, ((n - c) // (b - c)))
	return(max((n // a), (g + ((n - (g * (b - c))) // a))))
