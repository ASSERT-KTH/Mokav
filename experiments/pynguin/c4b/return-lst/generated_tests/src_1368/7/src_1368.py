def func(*args):
	ret_values = []
	
	import math
	(n, m, k) = map(int, args[0].split())
	r = math.ceil((k / (2 * m)))
	d = math.ceil(((k - ((2 * m) * (r - 1))) / 2))
	if ((k % 2) == 0):
	    ret_values.append(r, d, 'R')
	else:
	    ret_values.append(r, d, 'L')

	return ret_values
