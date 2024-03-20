def func(*args):
	
	(a, b) = map(int, args[0].split())
	(c, d) = map(int, args[1].split())
	v = (set(range(b, (100 ** 2), a)) & set(range(d, (100 ** 2), c)))
	return((min(v) if v else (- 1)))
