def func(*args):
	
	from math import *
	a = abs(int(args[0]))
	n = max((floor(sqrt((2 * a))) - 1), 0)
	while ((((n * (n + 1)) // 2) < a) or (((((n * (n + 1)) // 2) - a) % 2) == 1)):
	    n += 1
	return(n)
