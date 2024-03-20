def func(*args):
	
	import math
	(x, y, n) = map(int, args[0].split())
	best = (0, 0)
	mingap = (10 ** 9)
	eps = 1e-15
	for i in range(1, (n + 1)):
	    m = ((i * x) / y)
	    m1 = math.floor(m)
	    m2 = math.ceil(m)
	    gap1 = abs(((x / y) - (m1 / i)))
	    gap2 = abs(((x / y) - (m2 / i)))
	    if (gap1 < (mingap - eps)):
	        mingap = gap1
	        best = (m1, i)
	    if (gap2 < (mingap - eps)):
	        mingap = gap2
	        best = (m2, i)
	return(*best, sep='/')
