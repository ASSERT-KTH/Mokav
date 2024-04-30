def original_func(*args):
	global_list = []
	
	a = list(map(int, args[0].split()))
	if (((a[0] * a[2]) * a[4]) < ((a[1] * a[3]) * a[5])):
	    global_list.append('Ron')
	elif ((0 == ((a[0] * a[2]) * a[4])) ^ (0 == ((a[1] * a[3]) * a[5]))):
	    global_list.append('Hermione')
	elif (0 == ((a[0] * a[2]) * a[4]) == ((a[1] * a[3]) * a[5])):
	    if ((a[2] == 0) and (a[3] != 0)):
	        global_list.append('Ron')
	    else:
	        global_list.append('Hermione')
	else:
	    global_list.append('Hermione')
	return global_list