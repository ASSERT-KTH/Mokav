def func(*args):
	
	(x, y, z, k) = map(int, args[0].split())
	(x, y, z) = sorted((x, y, z))
	a = min((k // 3), (x - 1))
	b = min(((k - a) // 2), (y - 1))
	c = min(((k - a) - b), (z - 1))
	return((((a + 1) * (b + 1)) * (c + 1)))
