def original_func(*args):
	global_list = []
	
	a = list(map(int, args[0].split()))
	a.sort()
	if ((a[3] < (a[0] + a[1])) or (a[3] < (a[0] + a[2])) or (a[3] < (a[2] + a[1]))):
	    global_list.append('TRIANGLE')
	elif ((a[3] == (a[0] + a[1])) or (a[3] == (a[0] + a[2])) or (a[3] == (a[2] + a[1]))):
	    global_list.append('SEGMENT')
	elif (a[2] < (a[0] + a[1])):
	    global_list.append('TRIANGLE')
	elif (a[2] == (a[0] + a[1])):
	    global_list.append('SEGMENT')
	else:
	    global_list.append('IMPOSSIBLE')
	return global_list