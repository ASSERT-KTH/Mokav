def func(*args):
	ret_values = []
	
	import sys
	import math
	n = int(sys.stdin.readline())
	a = []
	a.append(str(n))
	for i in range(1, n):
	    a.append(str(i))
	ret_values.append(' '.join(a))

	return ret_values
