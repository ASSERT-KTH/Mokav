def func(*args):
	
	(n, k, m) = map(int, args[0].split())
	return(((n - max((k + 1), (n - m))) + 1))
