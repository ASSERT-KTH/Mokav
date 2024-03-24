def func(*args):
	
	(n, m, k) = map(int, args[0].split())
	return((max(n, m, k) - min(n, m, k)))
