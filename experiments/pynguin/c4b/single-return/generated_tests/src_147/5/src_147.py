def func(*args):
	
	'input\n0\n'
	n = int(args[0])
	return(([8, 4, 2, 6][((n % 4) - 1)] if (n != 0) else 1))
