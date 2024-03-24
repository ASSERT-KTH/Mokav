def func(*args):
	
	(a, b) = map(int, args[0].split())
	return((((a + b) - 1) - min(a, b)), min(a, b))
