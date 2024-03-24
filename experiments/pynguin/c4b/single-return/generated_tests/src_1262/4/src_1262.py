def func(*args):
	
	(a, b, ab) = map(int, args[0].split())
	return(min(((a + b) + ab), ((2 * a) + (2 * b)), ((2 * a) + (2 * ab)), ((2 * b) + (2 * ab))))
