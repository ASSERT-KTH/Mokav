def func(*args):
	
	(d1, d2, d3) = map(int, args[0].split())
	return(((min(d1, d2) + min((d1 + d2), d3)) + min(max(d1, d2), (d3 + min(d1, d2)))))
