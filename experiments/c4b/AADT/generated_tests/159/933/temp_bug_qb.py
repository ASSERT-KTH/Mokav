def original_func(*args):
	global_list = []
	
	a = list(args[0].split())
	x = int(a[0])
	y = 0
	if ('week' in a):
	    if ((x == 6) or (x == 7)):
	        y = 53
	    else:
	        y = 52
	if ('month' in a):
	    if (x == 31):
	        y = 7
	    elif (x == 30):
	        y = 11
	    elif (x <= 29):
	        y = 12
	global_list.append(y)
	return global_list