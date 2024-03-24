def func(*args):
	
	import sys
	import math
	(a, b) = map(int, sys.stdin.readline().split())
	return(math.floor(((int(a) * int(b)) / 2)))
