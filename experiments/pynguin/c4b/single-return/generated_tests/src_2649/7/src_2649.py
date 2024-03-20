def func(*args):
	
	n = int(args[0])
	v = (((n // 2) - 1) if ((n % 2) == 0) else (n // 2))
	return(v)
