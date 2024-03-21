def func(*args):
	ret_values = []
	
	import math
	n = int(args[0])
	s = (2 * n)
	t = (math.sqrt((1 + (4 * s))) - 1)
	if ((t % 2) == 0):
	    ret_values.append('YES')
	else:
	    ret_values.append('NO')

	return ret_values
