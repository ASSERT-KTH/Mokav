def func(*args):
	
	(d1, d2, d3) = [int(x) for x in args[0].split(' ')]
	return(min(((2 * d1) + (2 * d2)), ((d1 + d2) + d3), ((2 * d2) + (2 * d3)), ((2 * d1) + (2 * d3))))
