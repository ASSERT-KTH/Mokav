def func(*args):
	ret_values = []
	
	import math
	(n, x, y) = map(int, args[0].split(' '))
	ret_values.append(max(0, math.ceil((((y * n) / 100) - x))))

	return ret_values
