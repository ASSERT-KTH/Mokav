def func(*args):
	
	(n, m) = map(int, args[0].split())
	return(((pow(3, n, m) - 1) % m))
