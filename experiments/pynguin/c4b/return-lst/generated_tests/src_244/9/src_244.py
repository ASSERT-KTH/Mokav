def func(*args):
	ret_values = []
	
	(a, b) = map(int, args[0].split())
	(c, d) = map(int, args[1].split())
	v = (set(range(b, (100 ** 2), a)) & set(range(d, (100 ** 2), c)))
	ret_values.append((min(v) if v else (- 1)))

	return ret_values
