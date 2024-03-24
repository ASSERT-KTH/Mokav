def func(*args):
	
	(a, b, r) = map(int, args[0].split())
	return(('Second' if ((a < (2 * r)) or (b < (2 * r))) else 'First'))
