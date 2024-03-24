def func(*args):
	ret_values = []
	
	import sys
	(n, m) = map(float, args[0].split())
	ret_values.append(round(((n * m) // 2)))

	return ret_values
