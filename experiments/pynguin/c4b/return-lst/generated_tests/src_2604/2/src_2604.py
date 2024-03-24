def func(*args):
	ret_values = []
	
	import math
	n = int(args[0])
	ret_values.append((math.ceil((n / 2)) - 1))

	return ret_values
