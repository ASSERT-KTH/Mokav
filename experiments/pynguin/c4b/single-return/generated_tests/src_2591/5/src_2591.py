def func(*args):
	
	n = args[0]
	years = [int(s) for s in args[1].split()]
	return((sum(years) // int(n)))
