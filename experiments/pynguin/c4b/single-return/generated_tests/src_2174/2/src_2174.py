def func(*args):
	
	(r, g, b) = map(int, args[0].split())
	return((max((3 * ((r - 1) // 2)), (1 + (3 * ((g - 1) // 2))), (2 + (3 * ((b - 1) // 2)))) + 30))
