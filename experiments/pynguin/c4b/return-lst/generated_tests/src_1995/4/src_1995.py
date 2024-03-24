def func(*args):
	ret_values = []
	
	import math
	(l, d, k) = map(int, args[0].split())
	eachLane = (2 * d)
	lane = math.ceil((float(k) / eachLane))
	desk = math.ceil(((k % (2 * d)) / 2.0))
	if (desk == 0):
	    desk = d
	if ((k % 2) == 0):
	    ret_values.append(int(lane), int(desk), 'R')
	else:
	    ret_values.append(int(lane), int(desk), 'L')

	return ret_values
