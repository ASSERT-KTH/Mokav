def func(*args):
	
	(c, v0, v1, a, l) = map(int, args[0].split())
	d = 0
	while (c > 0):
	    c -= (min((v0 + (a * d)), v1) - (l * (d > 0)))
	    d += 1
	return(d)
