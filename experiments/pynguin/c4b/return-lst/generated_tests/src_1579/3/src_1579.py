def func(*args):
	ret_values = []
	
	import sys
	(a, b) = map(int, sys.stdin.readline().split())
	i = 0
	if (a == b):
	    ret_values.append(1)
	else:
	    while (a <= b):
	        i += 1
	        a *= 3
	        b *= 2
	    ret_values.append(i)

	return ret_values
