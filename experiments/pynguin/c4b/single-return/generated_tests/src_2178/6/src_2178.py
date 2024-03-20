def func(*args):
	
	import math
	(a, b, c) = map(int, args[0].split(' '))
	return(max(math.ceil((((a * c) / 100) - b)), 0))
