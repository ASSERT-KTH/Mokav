def func(*args):
	
	(n, k) = map(int, args[0].split())
	return(max(((3 * n) - k), 0))
