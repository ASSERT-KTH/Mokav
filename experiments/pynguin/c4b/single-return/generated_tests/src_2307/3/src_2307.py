def func(*args):
	
	n = args[0]
	return([n, n.swapcase()][(n[1:] == n[1:].upper())])
