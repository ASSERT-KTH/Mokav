def func(*args):
	
	import sys
	(a, b, c) = [int(x) for x in sys.stdin.readline().split()]
	return(((b * c) + (((b + c) - 1) * (a - 1))))
