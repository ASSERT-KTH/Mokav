def patched_func(*args):
	global_list = []
	
	from math import *
	(n, k) = map(int, args[0].split(' '))
	if (n == 1):
	    global_list.append(0)
	    exit(0)
	if ((k + 1) == n):
	    global_list.append(2)
	    exit(0)
	if (k >= n):
	    global_list.append(1)
	    exit(0)
	d = ((((2 * k) - 3) ** 2) + (8 * (k - n)))
	if (d < 0):
	    global_list.append((- 1))
	    exit(0)
	if (d == 0):
	    x1 = (((2 * k) - 3) / 2)
	    if ((x1 < 0) or (ceil(x1) > (k - 2))):
	        global_list.append((- 1))
	    elif (x1 == ceil(x1)):
	        global_list.append((x1 + 2))
	    else:
	        global_list.append((ceil(x1) + 1))
	    exit(0)
	x1 = ((((2 * k) - 3) - sqrt(d)) / 2)
	x2 = ((((2 * k) - 3) + sqrt(d)) / 2)
	if (x1 <= 0):
	    if ((x2 <= 0) or (ceil(x2) > (k - 2))):
	        global_list.append((- 1))
	    elif (x1 == ceil(x1)):
	        global_list.append((x1 + 2))
	    else:
	        global_list.append((ceil(x1) + 1))
	elif ((x1 <= 0) or (ceil(x1) > (k - 2))):
	    global_list.append((- 1))
	else:
	    global_list.append((ceil(x1) + 1))
	return global_list