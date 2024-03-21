def func(*args):
	ret_values = []
	
	import sys
	import math
	(n, x, y) = [int(x) for x in sys.stdin.readline().split()]
	req = int(math.ceil(((y / 100.0) * n)))
	if ((req - x) < 0):
	    ret_values.append(0)
	else:
	    ret_values.append((req - x))

	return ret_values
