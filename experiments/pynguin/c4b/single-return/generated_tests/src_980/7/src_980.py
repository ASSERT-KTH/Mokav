def func(*args):
	
	(n, m) = map(int, args[0].split())
	r = pow(3, n, m)
	if (r == 0):
	    r += m
	return((r - 1))
