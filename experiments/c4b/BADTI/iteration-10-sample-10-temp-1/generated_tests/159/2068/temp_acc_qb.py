def patched_func(*args):
	global_list = []
	
	s = args[0].split()
	a = list(s)
	a[0] = int(a[0])
	if (a[2] == 'week'):
	    if ((a[0] > 4) and (a[0] < 7)):
	        global_list.append(53)
	    else:
	        global_list.append(52)
	elif (a[0] == 30):
	    global_list.append(11)
	elif (a[0] == 31):
	    global_list.append(7)
	else:
	    global_list.append(12)
	return global_list