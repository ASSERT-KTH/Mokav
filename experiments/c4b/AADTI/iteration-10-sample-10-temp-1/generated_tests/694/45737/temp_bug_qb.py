def original_func(*args):
	global_list = []
	
	position = args[0]
	result = (((int(position[0], 18) - 10) % 7) | ((int(position[1]) - 1) % 7))
	if (result == 0):
	    global_list.append(3)
	elif ((result == 3) or (result == 4)):
	    global_list.append(5)
	else:
	    global_list.append(8)
	return global_list