def func(*args):
	ret_values = []
	
	import math
	(a, b) = map(int, args[0].split())
	for var in range(1, 1000):
	    if ((a * pow(3, var)) > (b * pow(2, var))):
	        ret_values.append(var)
	        break

	return ret_values
