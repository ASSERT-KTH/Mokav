def func(*args):
	
	(a, b, c) = sorted(list(map(int, args[0].split())))
	return(min(((a + b) << 1), ((a + b) + c)))
