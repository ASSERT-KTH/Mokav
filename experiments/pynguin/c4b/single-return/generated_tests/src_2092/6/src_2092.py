def func(*args):
	
	from math import ceil
	(n, m, a) = map(int, args[0].split())
	return((ceil((n / a)) * ceil((m / a))))
