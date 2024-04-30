def original_func(*args):
	global_list = []
	
	x = args[0]
	y = x.capitalize()
	caps = x.upper()
	first = x[0]
	last = x[1:(len(x) - 1)]
	nocaps = x.lower()
	if ((x != caps) and (x != nocaps)):
	    if ((x == y) or ((first == first.lower()) and (last == last.upper()))):
	        global_list.append(y)
	    else:
	        global_list.append(x)
	elif ((len(x) == 1) and (x == nocaps)):
	    global_list.append(caps)
	elif ((len(x) == 1) and (x == caps)):
	    global_list.append(nocaps)
	elif (x == caps):
	    global_list.append(nocaps)
	elif (x == nocaps):
	    global_list.append(x)
	return global_list