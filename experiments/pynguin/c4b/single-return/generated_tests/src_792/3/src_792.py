def func(*args):
	
	import sys
	import math
	(n, m) = map(int, args[0].split())
	
	def ans(nn):
	    return(nn)
	    sys.exit()
	if (n <= m):
	    ans(n)
	C = n
	if (n < 100000):
	    d = 0
	    while (n > 0):
	        d += 1
	        n = (min(C, (n + m)) - d)
	    ans(d)
	t = (n - m)
	if (t < 100000000):
	    k = 0
	    while (((k * (k + 1)) / 2) < t):
	        k += 1
	    ans((m + k))
	from decimal import *
	import decimal
	getcontext().prec = 19
	k = (Decimal(int((2 * Decimal(t)).sqrt())) - 10)
	while (((Decimal(k) * (Decimal(k) + 1)) / 2) < Decimal(t)):
	    k = (Decimal(k) + 1)
	ans((Decimal(m) + k))
