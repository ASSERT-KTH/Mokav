def func(*args):
	
	(x, y, z) = map(int, args[0].split())
	return((4 * int((((((x * y) // z) ** 0.5) + (((x * z) // y) ** 0.5)) + (((z * y) // x) ** 0.5)))))
