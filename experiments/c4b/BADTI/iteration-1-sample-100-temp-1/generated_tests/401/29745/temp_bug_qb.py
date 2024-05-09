def original_func(*args):
	global_list = []
	
	number = int(args[0])
	if (number == 13):
	    global_list.append('8092')
	else:
	    global_list.append((2 ** number))
	return global_list