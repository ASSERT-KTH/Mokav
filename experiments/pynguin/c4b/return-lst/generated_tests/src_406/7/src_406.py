def func(*args):
	ret_values = []
	
	import math
	string = args[0]
	(a, b, c) = map(int, string.split())
	(p, q) = ((math.ceil(((a + 1) / b)) * b), ((c // b) * b))
	if (p > c):
	    ret_values.append((- 1))
	else:
	    for x in range(p, (q + 1), b):
	        ret_values.append((x - a), end=' ')

	return ret_values
