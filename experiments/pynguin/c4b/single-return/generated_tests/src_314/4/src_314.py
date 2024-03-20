def func(*args):
	
	import sys
	import math
	(a, b) = map(int, args[0].split())
	return(min(a, b), ((max(a, b) - min(a, b)) // 2))
