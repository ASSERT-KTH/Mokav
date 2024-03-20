def func(*args):
	
	(a, b) = map(int, args[0].split())
	x = min(a, b)
	a -= x
	b -= x
	y = ((a // 2) + (b // 2))
	return(((str(x) + ' ') + str(y)))
