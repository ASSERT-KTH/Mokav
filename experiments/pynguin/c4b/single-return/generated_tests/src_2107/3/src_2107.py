def func(*args):
	
	from math import *
	(n, m, a) = map(float, args[0].strip().split())
	return((ceil((n / a)) + (ceil(((m - a) / a)) * ceil((n / a)))))
