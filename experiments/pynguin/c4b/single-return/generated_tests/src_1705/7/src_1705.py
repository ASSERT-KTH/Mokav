def func(*args):
	
	(a, b, c, d) = (int(args[0]), int(args[1]), int(args[2]), int(args[3]))
	e = ((a ^ b) and (c or d))
	f = ((b and c) or (a ^ d))
	return((e ^ f))
