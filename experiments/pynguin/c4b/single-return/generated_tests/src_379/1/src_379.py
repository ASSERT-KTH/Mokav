def func(*args):
	
	import math
	n = int(args[0])
	a = (math.sqrt(((n * 2) + 0.25)) - 0.5)
	if (int(a) == a):
	    a = (int(a) - 1)
	else:
	    a = int(a)
	return((n - ((a * (a + 1)) // 2)))
