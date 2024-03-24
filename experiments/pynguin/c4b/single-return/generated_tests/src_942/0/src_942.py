def func(*args):
	
	(n, a, b) = map(int, str(args[0]).strip().split())
	return(((n - max((a + 1), (n - b), 1)) + 1))
