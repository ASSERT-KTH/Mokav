def original_func(*args):
	global_list = []
	
	s = args[0]
	n = int(args[1])
	a = ['v', '<', '^', '>']
	k = (n % 4)
	if (k == 2):
	    global_list.append('undefined')
	elif (((4 - a.index(s[2])) + a.index(s[0])) > 0):
	    global_list.append('cw')
	else:
	    global_list.append('ccw')
	return global_list