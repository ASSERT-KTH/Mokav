def func(*args):
	
	(a, b, c) = map(int, args[0].split())
	return(min((2 * min(((a + b), (b + c), (c + a)))), ((a + b) + c)))
