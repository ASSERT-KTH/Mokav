def func(*args):
	ret_values = []
	
	import math
	(a, b, c) = map(int, args[0].split(' '))
	ret_values.append(max(math.ceil((((a * c) / 100) - b)), 0))

	return ret_values
