def func(*args):
	ret_values = []
	
	import sys
	import math
	(a, b) = map(int, args[0].split())
	ret_values.append(min(a, b), ((max(a, b) - min(a, b)) // 2))

	return ret_values
