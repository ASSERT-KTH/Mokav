def func(*args):
	ret_values = []
	
	(n, m) = map(int, args[0].split())
	import math
	x = 0
	for i in range((round(math.sqrt(n)) + 1)):
	    if (((m - ((n - (i ** 2)) ** 2)) == i) and ((n - (i ** 2)) >= 0)):
	        x += 1
	ret_values.append(x)

	return ret_values
