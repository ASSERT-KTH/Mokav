def patched_func(*args):
	global_list = []
	
	import math
	(n, x1, y1, x2, y2) = [int(i) for i in args[0].split()]
	obw = (4 * n)
	dist_from_zero1 = 0
	dist_from_zero2 = 0
	if ((x1 == 0) and (y1 >= 0)):
	    dist_from_zero1 = (x1 + y1)
	elif ((y1 == n) and (x1 != 0)):
	    dist_from_zero1 = (n + x1)
	elif ((x1 >= 0) and (y1 == 0)):
	    dist_from_zero1 = (obw - x1)
	elif ((y1 != 0) and (x1 == n)):
	    dist_from_zero1 = ((3 * n) - y1)
	if ((x2 == 0) and (y2 >= 0)):
	    dist_from_zero2 = (x2 + y2)
	elif ((y2 == n) and (x2 != 0)):
	    dist_from_zero2 = (n + x2)
	elif ((x2 >= 0) and (y2 == 0)):
	    dist_from_zero2 = (obw - x2)
	elif ((y2 != 0) and (x2 == n)):
	    dist_from_zero2 = ((3 * n) - y2)
	global_list.append(min(int(math.fabs((dist_from_zero2 - dist_from_zero1))), int(((obw - dist_from_zero1) + dist_from_zero2)), int(((obw - dist_from_zero2) + dist_from_zero1))))
	return global_list