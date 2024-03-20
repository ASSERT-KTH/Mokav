def func(*args):
	
	n = int(args[0])
	return(((n // 5) if ((n % 5) == 0) else ((n // 5) + 1)))
