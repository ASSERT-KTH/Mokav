def func(*args):
	
	import math
	(n, x, y) = map(int, args[0].split(' '))
	return(max(0, math.ceil((((y * n) / 100) - x))))
