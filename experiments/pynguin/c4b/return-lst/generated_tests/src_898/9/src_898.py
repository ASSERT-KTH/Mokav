def func(*args):
	ret_values = []
	
	import math
	a = float(args[0])
	ret_values.append(math.ceil((a / 5)))

	return ret_values
