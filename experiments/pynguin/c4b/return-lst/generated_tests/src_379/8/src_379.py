def func(*args):
	ret_values = []
	
	import math
	n = int(args[0])
	a = (math.sqrt(((n * 2) + 0.25)) - 0.5)
	if (int(a) == a):
	    a = (int(a) - 1)
	else:
	    a = int(a)
	ret_values.append((n - ((a * (a + 1)) // 2)))

	return ret_values
