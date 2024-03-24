def func(*args):
	
	(n, k, l, c, d, p, nl, np) = map(int, args[0].split())
	total_toast = min(((k * l) / nl), (c * d), (p / np))
	return(int((total_toast / n)))
