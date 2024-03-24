def func(*args):
	
	(n, x, y) = (int(x) for x in args[0].split())
	return(max(0, (- (((100 * x) - (n * y)) // 100))))
