def func(*args):
	ret_values = []
	
	import math
	(h1, h2) = map(int, args[0].split())
	(r, f) = map(int, args[1].split())
	if ((h1 + (r * 8)) >= h2):
	    ret_values.append(0)
	elif (f >= r):
	    ret_values.append((- 1))
	else:
	    ret_values.append(math.ceil((((h2 - h1) - (8 * r)) / (12 * (r - f)))))

	return ret_values
