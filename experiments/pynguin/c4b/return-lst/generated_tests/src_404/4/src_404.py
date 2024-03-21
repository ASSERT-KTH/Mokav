def func(*args):
	ret_values = []
	
	import math
	string = args[0]
	(n, x, y) = map(int, string.split())
	a = math.ceil(((y / 100) * n))
	if (a < x):
	    ret_values.append(0)
	else:
	    ret_values.append((a - x))

	return ret_values
