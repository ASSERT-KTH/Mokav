def func(*args):
	ret_values = []
	
	import sys
	(a, b, c) = [int(x) for x in sys.stdin.readline().split()]
	ret_values.append(((b * c) + (((b + c) - 1) * (a - 1))))

	return ret_values
