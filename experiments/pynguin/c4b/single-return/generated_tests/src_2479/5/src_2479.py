def func(*args):
	
	import math
	inp = args[0].split()
	n = int(inp[0])
	a = int(inp[1])
	val = math.inf
	v3 = 1
	for i in range(1, (n - 1)):
	    if (val > abs((((180 / n) * i) - a))):
	        v3 = i
	        val = abs((((180 / n) * i) - a))
	return(2, 1, (v3 + 2))
