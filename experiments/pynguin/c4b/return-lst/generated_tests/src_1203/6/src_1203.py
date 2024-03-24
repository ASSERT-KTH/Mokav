def func(*args):
	ret_values = []
	
	import sys
	import math
	(n, k) = [int(x) for x in sys.stdin.readline().split()]
	if ((k == 1) and (n == 1)):
	    ret_values.append('a')
	    exit()
	if ((k == 1) or (k > n)):
	    ret_values.append((- 1))
	    exit()
	res = []
	t = 2
	for i in range(n):
	    if ((n - (k - 2)) > i):
	        if ((i % 2) == 0):
	            res.append('a')
	        else:
	            res.append('b')
	    else:
	        res.append(chr((t + 97)))
	        t += 1
	ret_values.append(''.join(res))

	return ret_values
