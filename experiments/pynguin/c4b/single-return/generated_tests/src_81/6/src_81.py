def func(*args):
	
	(n, m) = [int(i) for i in args[0].split()]
	d = ((n * (n + 1)) // 2)
	dk = (m // d)
	c = (m - (dk * d))
	i = 1
	while (c >= i):
	    c = (c - i)
	    i = (i + 1)
	return(c)
