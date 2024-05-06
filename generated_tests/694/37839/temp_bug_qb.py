def original_func(*args):
	global_list = []
	
	a = args[0]
	b = int(a[(- 1)])
	a = a[0:(- 1)]
	if ((a != 'h') and (a != 'a') and (b != 1) and (b != 8)):
	    global_list.append(8)
	elif ((a == 'h') or ((a == 'a') and (b != 1) and (b != 8))):
	    global_list.append(5)
	elif (((a != 'h') and (a != 'a') and (b == 1)) or (b == 8)):
	    global_list.append(5)
	else:
	    global_list.append(3)
	return global_list