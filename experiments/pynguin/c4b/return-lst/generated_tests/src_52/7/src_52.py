def func(*args):
	ret_values = []
	
	import math
	(n, m, s) = map(int, args[0].split())
	c = 0
	cc = 0
	su = 0
	ss = 0
	if (((s >= m) and (s >= n)) or (s == 1) or (((m % s) == 0) and ((n % s) == 0))):
	    ret_values.append((m * n))
	else:
	    ret_values.append(((((((n - 1) // s) + 1) * (((n - 1) % s) + 1)) * (((m - 1) // s) + 1)) * (((m - 1) % s) + 1)))

	return ret_values
