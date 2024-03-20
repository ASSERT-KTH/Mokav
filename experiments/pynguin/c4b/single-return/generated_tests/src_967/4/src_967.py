def func(*args):
	
	'\n\nCreated on 20160607\n\n\n\n@author: ChronoCorax\n\n'
	(n, k) = [int(c) for c in args[0].split()]
	c = (n - (2 * k))
	if (c < 0):
	    c = 0
	a = (((n * (n - 1)) // 2) - ((c * (c - 1)) // 2))
	return(a)
