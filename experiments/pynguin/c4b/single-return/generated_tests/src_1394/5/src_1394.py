def func(*args):
	
	n = int(args[0])
	res = ((2 * (n // 3)) + ((n % 3) > 0))
	return(res)
