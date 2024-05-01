def original_func(*args):
	global_list = []
	
	a = [int(x) for x in args[0].split(' ')]
	if (a[0] == max(a)):
	    global_list.append(((a[1] * 2) + (a[2] * 2)))
	elif (a[1] == max(a)):
	    global_list.append(((a[0] * 2) + (a[2] * 2)))
	else:
	    global_list.append(((a[0] * 2) + (a[1] * 2)))
	return global_list