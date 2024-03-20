def func(*args):
	
	n = int(args[0])
	m = (n // 7)
	l = (n - (m * 7))
	return(((m * 2) + (l == 6)), (((m * 2) + (l > 0)) + (l > 1)))
