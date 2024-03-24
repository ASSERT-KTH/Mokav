def func(*args):
	ret_values = []
	
	import math
	n = int(args[0].strip())
	if ((n % 2) != 0):
	    ret_values.append(0)
	else:
	    ret_values.append((math.ceil((n / 4)) - 1))

	return ret_values
