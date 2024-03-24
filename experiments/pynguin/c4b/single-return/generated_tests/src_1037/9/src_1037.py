def func(*args):
	
	(d1, d2, d3) = [int(s) for s in args[0].split()]
	return(min(((d1 + d2) + d3), (2 * (d1 + d2)), (2 * (d1 + d3)), (2 * (d3 + d2))))
