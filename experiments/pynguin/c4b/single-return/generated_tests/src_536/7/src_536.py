def func(*args):
	
	(d1, d2, d3) = map(int, args[0].split())
	a = ((d1 + d2) * 2)
	b = ((d1 + d3) * 2)
	c = ((d1 + d3) + d2)
	d = ((d2 + d3) * 2)
	return(min(a, b, c, d))
