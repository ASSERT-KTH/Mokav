def func(*args):
	
	(a, b, c) = map(int, args[0].split())
	k = (((a * b) * c) ** 0.5)
	return((4 * int((((k / a) + (k / b)) + (k / c)))))
