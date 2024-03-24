def func(*args):
	
	import math
	n = int(args[0])
	queue = ['Sheldon', 'Leonard', 'Penny', 'Rajesh', 'Howard']
	c = 1
	while ((5 * c) < n):
	    n -= (5 * c)
	    c *= 2
	return(queue[((n - 1) // c)])
