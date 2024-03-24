def func(*args):
	ret_values = []
	
	from math import *
	a = args[0].split()
	if (a[2] == 'week'):
	    if ((a[0] == '5') or (a[0] == '6')):
	        ret_values.append(53)
	    else:
	        ret_values.append(52)
	if (a[2] == 'month'):
	    if (a[0] == '31'):
	        ret_values.append(7)
	    elif (a[0] == '30'):
	        ret_values.append(11)
	    else:
	        ret_values.append(12)

	return ret_values
