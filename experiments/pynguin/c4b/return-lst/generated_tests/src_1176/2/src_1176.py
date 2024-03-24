def func(*args):
	ret_values = []
	
	from math import *
	(n, k) = map(int, args[0].split(' '))
	if (n == 1):
	    ret_values.append(0)
	    exit(0)
	if ((k + 1) == n):
	    ret_values.append(2)
	    exit(0)
	if (k >= n):
	    ret_values.append(1)
	    exit(0)
	d = ((((2 * k) - 3) ** 2) + (8 * (k - n)))
	if (d < 0):
	    ret_values.append((- 1))
	    exit(0)
	if (d == 0):
	    x1 = (((2 * k) - 3) / 2)
	    if ((x1 < 0) or (ceil(x1) > (k - 2))):
	        ret_values.append((- 1))
	    elif (x1 == ceil(x1)):
	        ret_values.append((x1 + 2))
	    else:
	        ret_values.append((ceil(x1) + 1))
	    exit(0)
	x1 = ((((2 * k) - 3) - sqrt(d)) / 2)
	x2 = ((((2 * k) - 3) + sqrt(d)) / 2)
	if (x1 <= 0):
	    if ((x2 <= 0) or (ceil(x2) > (k - 2))):
	        ret_values.append((- 1))
	    elif (x1 == ceil(x1)):
	        ret_values.append((x1 + 2))
	    else:
	        ret_values.append((ceil(x1) + 1))
	elif ((x1 <= 0) or (ceil(x1) > (k - 2))):
	    ret_values.append((- 1))
	else:
	    ret_values.append((ceil(x1) + 1))

	return ret_values
