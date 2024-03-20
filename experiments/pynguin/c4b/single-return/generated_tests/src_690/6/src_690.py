def func(*args):
	
	n = int(args[0])
	p = ((9 ** n) * (3 ** n))
	return(((p - (7 ** n)) % 1000000007))
