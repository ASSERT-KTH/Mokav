def func(*args):
	
	n = int(args[0])
	return(((((n // 2) - 1) // 2) if ((n != 1) and ((n % 2) == 0)) else 0))
