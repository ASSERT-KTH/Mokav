def func(*args):
	
	f = (lambda a, b: (a if (b == 0) else f(b, (a % b))))
	(a, b, n) = map(int, args[0].split())
	c = 1
	while (n > 0):
	    c = (0 if c else 1)
	    n -= (f(b, n) if c else f(a, n))
	return(c)
