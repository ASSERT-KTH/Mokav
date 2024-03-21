def func(*args):
	ret_values = []
	
	import math
	(a, b) = map(int, args[0].split())
	ret_values.append(int(math.log(((1.5 * b) / a), 1.5)))

	return ret_values
