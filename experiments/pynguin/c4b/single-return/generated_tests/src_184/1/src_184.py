def func(*args):
	
	n = int(args[0])
	mod = 1000000007
	return((int(((pow(3, n, (4 * mod)) + (3 * ((- 1) ** n))) / 4)) % (4 * mod)))
