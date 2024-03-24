def func(*args):
	
	import math
	n = int(args[0])
	return([(math.ceil((n / 4)) - 1), 0][((n % 2) != 0)])
