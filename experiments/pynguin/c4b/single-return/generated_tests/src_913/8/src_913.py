def func(*args):
	
	n = int(args[0])
	return(((- 1) if (n < 3) else (210 * (((10 ** (n - 1)) // 210) + 1))))
