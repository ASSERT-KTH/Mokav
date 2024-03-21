def func(*args):
	ret_values = []
	
	(n, k) = [int(x) for x in args[0].split(' ')]
	a = (n // (2 * (1 + k)))
	b = (a * k)
	c = (n - (a + b))
	ret_values.append(('%d %d %d' % (a, b, c)))

	return ret_values
