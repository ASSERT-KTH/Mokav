def func(*args):
	
	from math import sqrt
	(a, b, c) = map(int, args[0].split())
	s = int(sqrt(((a * b) * c)))
	return(((((s // a) + (s // b)) + (s // c)) * 4))
