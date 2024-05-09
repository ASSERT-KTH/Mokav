def original_func(*args):
	global_list = []
	
	from math import ceil
	(n, m, a) = [int(x) for x in args[0].split(' ')]
	modifier = 0
	if ((n == a) or (m == a)):
	    modifier = 1
	    global_list.append(((ceil((n / a)) + ceil((m / a))) - modifier))
	elif ((a > n) and (a > m)):
	    global_list.append(1)
	else:
	    global_list.append(((ceil((n / a)) + ceil((m / a))) - modifier))
	return global_list