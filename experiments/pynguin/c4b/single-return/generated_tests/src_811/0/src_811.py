def func(*args):
	
	(n, k, l, c, d, p, nl, np) = map(int, args[0].split())
	return(min(((k * l) // (n * nl)), ((c * d) // n), (p // (np * n))))
