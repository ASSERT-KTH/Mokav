def func(*args):
	
	n = int(args[0])
	return(((n // 2) if ((n % 2) == 1) else ((n // 2) - 1)))
