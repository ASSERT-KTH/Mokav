def func(*args):
	ret_values = []
	
	from math import *
	(n, m, a) = map(float, args[0].strip().split())
	ret_values.append((ceil((n / a)) + (ceil(((m - a) / a)) * ceil((n / a)))))

	return ret_values
