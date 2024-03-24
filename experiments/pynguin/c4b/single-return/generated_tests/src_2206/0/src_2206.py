def func(*args):
	
	(n, a, b) = map(int, args[0].split())
	return(((n - max((a + 1), (n - b))) + 1))
