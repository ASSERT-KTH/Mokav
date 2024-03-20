def func(*args):
	
	(n, k, l, c, d, p, nl, np) = map(int, args[0].split())
	l = (k * l)
	c = (d * c)
	return((min((p // np), c, (l // nl)) // n))
