def func(*args):
	ret_values = []
	
	from math import log
	from decimal import *
	getcontext().prec = 6
	k = int(args[0])
	l = int(args[1])
	ans = 0
	while ((l > 1) and ((l % k) == 0)):
	    l /= k
	    ans += 1
	if (l == 1):
	    ret_values.append('YES')
	    ret_values.append((ans - 1))
	else:
	    ret_values.append('NO')

	return ret_values
