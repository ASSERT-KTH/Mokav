def func(*args):
	ret_values = []
	
	from math import *
	(l, m, a) = args[0].split()
	l = int(l)
	m = int(m)
	a = int(a)
	r = ceil((l / a))
	k = ceil((m / a))
	ret_values.append((k * r))

	return ret_values
