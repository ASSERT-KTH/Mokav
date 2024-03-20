def func(*args):
	
	(x, y, z) = map(int, args[0].split())
	return(min((x - y), (z + 1)))
