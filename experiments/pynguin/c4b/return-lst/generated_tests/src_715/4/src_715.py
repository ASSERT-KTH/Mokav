def func(*args):
	ret_values = []
	
	(n, k, l, c, d, p, nl, np) = map(int, args[0].split())
	l = (k * l)
	c = (d * c)
	ret_values.append((min((p // np), c, (l // nl)) // n))

	return ret_values
