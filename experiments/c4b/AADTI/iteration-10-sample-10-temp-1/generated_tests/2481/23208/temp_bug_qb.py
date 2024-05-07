def original_func(*args):
	global_list = []
	
	import math
	n = int(args[0])
	queue = ['Sheldon', 'Leonard', 'Penny', 'Rajesh', 'Howard']
	c = 1
	while ((5 * c) < n):
	    c *= 2
	global_list.append(queue[((n - 1) // c)])
	return global_list