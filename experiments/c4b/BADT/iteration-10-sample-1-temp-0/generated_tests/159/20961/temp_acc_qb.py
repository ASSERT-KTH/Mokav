def patched_func(*args):
	global_list = []
	
	from math import *
	a = args[0].split()
	if (a[2] == 'week'):
	    if ((a[0] == '5') or (a[0] == '6')):
	        global_list.append(53)
	    else:
	        global_list.append(52)
	if (a[2] == 'month'):
	    if (a[0] == '31'):
	        global_list.append(7)
	    elif (a[0] == '30'):
	        global_list.append(11)
	    else:
	        global_list.append(12)
	return global_list