def func(*args):
	ret_values = []
	
	from math import inf
	(a, b) = [int(x) for x in args[0].split()]
	(c, d) = [int(x) for x in args[1].split()]
	if (b > d):
	    (a, c) = (c, a)
	    (b, d) = (d, b)
	r1 = ((d - b) % a)
	r2 = (c % a)
	k2s = [((r1 + (k2 * r2)) % a) for k2 in range(a)]
	if (0 not in k2s):
	    ret_values.append((- 1))
	else:
	    ret_values.append(((k2s.index(0) * c) + d))

	return ret_values
