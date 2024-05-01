def original_func(*args):
	global_list = []
	
	(s1, s2) = args[0].split()
	n = int(args[1])
	A = ['^', '>', 'v', '<']
	if ((n % 2) == 0):
	    global_list.append('undefined')
	elif (A[(A.index(s2) - 1)] == s1):
	    if ((n % 4) == 3):
	        global_list.append('ccw')
	    else:
	        global_list.append('cw')
	else:
	    global_list.append('ccw')
	return global_list