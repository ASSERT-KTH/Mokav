def func(*args):
	
	(n, m) = map(int, args[0].split())
	import math
	x = 0
	for i in range((round(math.sqrt(n)) + 1)):
	    if (((m - ((n - (i ** 2)) ** 2)) == i) and ((n - (i ** 2)) >= 0)):
	        x += 1
	return(x)
