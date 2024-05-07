def original_func(*args):
	global_list = []
	
	x = int(args[0])
	if (x >= 6):
	    i = ((x // 5) + 1)
	    global_list.append(str(i))
	else:
	    global_list.append('1')
	return global_list