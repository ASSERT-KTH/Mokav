def func(*args):
	ret_values = []
	
	import sys
	(l, r, k) = map(int, args[0].split())
	p = 1
	ans = 0
	while (p <= r):
	    if (p >= l):
	        ans += 1
	        ret_values.append(p, end=' ')
	    p *= k
	if (ans == 0):
	    ret_values.append((- 1))

	return ret_values
