def func(*args):
	
	import math
	import time
	st = args[0].split()
	n = int(st[0])
	k = int(st[1])
	a = (n // ((2 * k) + 2))
	if (a != 0):
	    b = (k * a)
	    c = ((n - a) - b)
	else:
	    b = 0
	    c = n
	return(a, b, c)
