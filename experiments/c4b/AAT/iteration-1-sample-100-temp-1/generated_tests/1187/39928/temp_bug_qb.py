def original_func(*args):
	global_list = []
	
	i = args[0]
	if ((i[0] == i[0].lower()) and (i[1:] == i[1:].upper())):
	    global_list.append((i[0].upper() + i[1:].lower()))
	elif (i.upper() == i):
	    global_list.append((i[0].upper() + i[1:].lower()))
	else:
	    global_list.append(i)
	return global_list