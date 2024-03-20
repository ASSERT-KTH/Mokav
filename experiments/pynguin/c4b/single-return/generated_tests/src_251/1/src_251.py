def func(*args):
	
	(x1, x2, x3) = map(int, args[0].split())
	return((max(x1, x2, x3) - min(x1, x2, x3)))
