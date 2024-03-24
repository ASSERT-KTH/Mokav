def func(*args):
	
	from math import *
	(l, m, a) = args[0].split()
	l = int(l)
	m = int(m)
	a = int(a)
	r = ceil((l / a))
	k = ceil((m / a))
	return((k * r))
