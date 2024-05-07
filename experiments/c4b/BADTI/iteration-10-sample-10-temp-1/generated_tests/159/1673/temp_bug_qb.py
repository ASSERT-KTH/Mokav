def original_func(*args):
	global_list = []
	
	n = args[0].split()
	if (n[(- 1)] == 'month'):
	    if (n[0] == '31'):
	        global_list.append(7)
	    elif (n[0] == '30'):
	        global_list.append(11)
	    elif (n[0] == '29'):
	        global_list.append(1)
	    else:
	        global_list.append(12)
	elif (n[0] in ['1', '2', '3', '4', '7']):
	    global_list.append(52)
	else:
	    global_list.append(53)
	return global_list