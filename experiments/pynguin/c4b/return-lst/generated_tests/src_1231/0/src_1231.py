def func(*args):
	ret_values = []
	
	import sys
	import math
	(a, b) = map(int, sys.stdin.readline().split())
	ret_values.append(math.floor(((int(a) * int(b)) / 2)))

	return ret_values
