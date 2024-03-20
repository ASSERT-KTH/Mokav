def func(*args):
	
	(x, y, z) = map(int, args[0].split())
	return(min(((x + y) + z), (2 * (x + y)), (2 * (y + z)), (2 * (x + z))))
