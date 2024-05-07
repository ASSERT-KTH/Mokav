def patched_func(*args):
	global_list = []
	
	import math
	n = int(args[0])
	x = 0
	y = 0
	while (n > x):
	    y += 1
	    x += (((10 ** (y - 1)) * 9) * y)
	x -= (((10 ** (y - 1)) * 9) * y)
	a = (((10 ** (y - 1)) + math.ceil(((n - x) / y))) - 1)
	b = ((n - x) % y)
	if (b == 0):
	    b = y
	a = str(a)
	global_list.append(a[(b - 1)])
	return global_list