def func(*args):
	ret_values = []
	
	from sys import stdin
	(l, r, k) = map(int, stdin.readline().split())
	res = 1
	p = 0
	get = 0
	while (res <= r):
	    if ((l == 1) and (get == 0)):
	        ret_values.append(1, '', end='')
	        get = 1
	        p = 1
	    res *= k
	    if (l <= res <= r):
	        ret_values.append(res, '', end='')
	        p = 1
	if (p == 0):
	    ret_values.append('-1')

	return ret_values
