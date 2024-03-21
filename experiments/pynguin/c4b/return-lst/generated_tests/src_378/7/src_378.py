def func(*args):
	ret_values = []
	
	import math
	string = args[0]
	(a, b, n) = map(int, string.split())
	p = 0
	while ((n ** p) < a):
	    p += 1
	q = 0
	while ((n ** q) < b):
	    q += 1
	if ((n ** q) > b):
	    q -= 1
	if (p > q):
	    ret_values.append((- 1))
	else:
	    for x in range(p, (q + 1)):
	        ret_values.append((n ** x), end=' ')

	return ret_values
