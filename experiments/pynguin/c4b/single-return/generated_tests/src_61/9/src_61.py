def func(*args):
	
	import math
	(b, g, t) = map(int, args[0].split())
	tot = 0
	for i in range(4, t):
	    if ((i <= b) and ((t - i) <= g)):
	        tot += ((math.factorial(b) // (math.factorial(i) * math.factorial((b - i)))) * (math.factorial(g) // (math.factorial((t - i)) * math.factorial(((g - t) + i)))))
	return(tot)
