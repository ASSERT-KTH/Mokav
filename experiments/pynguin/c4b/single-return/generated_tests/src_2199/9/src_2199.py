def func(*args):
	
	import sys
	(a, b, c) = map(int, args[0].split())
	return(((((a + b) - 1) * (c - 1)) + (a * b)))
