def func(*args):
	
	import math
	(a, b, n) = [int(i) for i in args[0].split()]
	l = 0
	while True:
	    minus = math.gcd(a, n)
	    if (n > minus):
	        n -= minus
	        l = 1
	    else:
	        l = 0
	        break
	    minus = math.gcd(b, n)
	    if (n > minus):
	        n -= minus
	        l = 0
	    else:
	        l = 1
	        break
	return(l)
