def func(*args):
	
	(n, k) = [int(x) for x in args[0].split(' ')]
	a = (n // (2 * (1 + k)))
	b = (a * k)
	c = (n - (a + b))
	return(('%d %d %d' % (a, b, c)))
