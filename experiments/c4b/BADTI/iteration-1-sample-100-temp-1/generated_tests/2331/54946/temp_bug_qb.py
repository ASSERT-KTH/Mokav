def original_func(*args):
	global_list = []
	
	import math
	(n, x1, y1, x2, y2) = [int(i) for i in args[0].split()]
	obw = (4 * n)
	dist_from_zero1 = 0
	dist_from_zero2 = 0
	if (x1 >= y1):
	    dist_from_zero1 = (x1 + y1)
	elif (x1 < y1):
	    dist_from_zero1 = ((obw - x1) - y1)
	if (x2 >= y2):
	    dist_from_zero2 = (x2 + y2)
	elif (x2 < y2):
	    dist_from_zero2 = ((obw - x2) - y2)
	global_list.append(min(int(math.fabs((dist_from_zero2 - dist_from_zero1))), int(((obw - dist_from_zero1) + dist_from_zero2))))
	return global_list