def func(*args):
	ret_values = []
	
	import sys
	(a, b, c) = map(int, args[0].split())
	ret_values.append(((((a + b) - 1) * (c - 1)) + (a * b)))

	return ret_values
