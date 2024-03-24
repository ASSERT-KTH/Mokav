def func(*args):
	
	(x, y) = map(int, args[0].split())
	return(int((int(((x / y) + 1)) * y)))
