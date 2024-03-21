def func(*args):
	ret_values = []
	
	import math
	a = int(args[0])
	b = int(math.sqrt((1 + (8 * a))))
	if ((b * b) != (1 + (8 * a))):
	    ret_values.append('NO')
	else:
	    ret_values.append('YES')

	return ret_values
