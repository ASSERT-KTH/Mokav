def func(*args):
	
	(l, b) = [int(x) for x in args[0].split()]
	n = 0
	while (b >= l):
	    n += 1
	    l = (3 * l)
	    b = (2 * b)
	return(n)
