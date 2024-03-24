def func(*args):
	
	(d1, d2, d3) = [int(i) for i in args[0].split()]
	return(min(min((2 * (d3 + d2)), (2 * (d1 + d3))), min((2 * (d1 + d2)), ((d1 + d2) + d3))))
