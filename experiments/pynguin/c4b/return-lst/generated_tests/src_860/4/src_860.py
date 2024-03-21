def func(*args):
	ret_values = []
	
	(x, y, z) = map(int, args[0].split())
	a = ((x + y) + z)
	b = (2 * (x + y))
	c = (2 * (x + z))
	d = (2 * (y + z))
	k = min(a, b, c, d)
	ret_values.append(k)

	return ret_values
