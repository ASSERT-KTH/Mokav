def func(*args):
	
	'input\n\n5\n\n'
	n = int(args[0])
	return(((n // 5) + (1 if (n % 5) else 0)))
