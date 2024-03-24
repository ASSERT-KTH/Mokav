def func(*args):
	ret_values = []
	
	import sys
	(y, k, n) = map(int, sys.stdin.readline().split())
	index = ((int((y / k)) * k) + k)
	x = 0
	while (index <= n):
	    x = (index - y)
	    index += k
	    if (x == 0):
	        continue
	    ret_values.append((str(x) + ' '), end='')
	if (x == 0):
	    ret_values.append('-1')

	return ret_values
