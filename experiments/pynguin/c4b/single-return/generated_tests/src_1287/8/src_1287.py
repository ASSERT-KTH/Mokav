def func(*args):
	
	(a, b, c) = map(int, args[0].split())
	return(min(((a + b) + c), ((2 * a) + (2 * b)), ((2 * a) + (2 * c)), ((2 * b) + (2 * c))))
