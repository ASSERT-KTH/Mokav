def func(*args):
	ret_values = []
	
	import math
	(h1, h2) = map(int, args[0].split())
	(a, b) = map(int, args[1].split())
	if ((h1 + (a * 8)) >= h2):
	    ret_values.append(0)
	elif (b >= a):
	    ret_values.append((- 1))
	else:
	    ret_values.append(math.ceil((((h2 - h1) - (8 * a)) / (12 * (a - b)))))

	return ret_values
