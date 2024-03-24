def func(*args):
	
	import math
	(a, b) = map(int, args[0].split())
	return(int(math.log(((1.5 * b) / a), 1.5)))
