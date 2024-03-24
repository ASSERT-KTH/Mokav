def func(*args):
	ret_values = []
	
	import math
	n = int(args[0])
	ret_values.append([(math.ceil((n / 4)) - 1), 0][((n % 2) != 0)])

	return ret_values
