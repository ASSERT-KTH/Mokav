def original_func(*args):
	global_list = []
	
	num = int(args[0])
	total = 2
	if (num == 0):
	    global_list.append(0)
	else:
	    for i in range((num - 1)):
	        total = (total * 2)
	    global_list.append(total)
	return global_list