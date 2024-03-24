def func(*args):
	
	n = int(args[0])
	return((((3 ** (3 * n)) - (7 ** n)) % (int(1000000000.0) + 7)))
