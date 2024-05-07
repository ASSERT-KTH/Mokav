def patched_func(*args):
	global_list = []
	
	position = args[0]
	col = ((int(position[0], 18) - 10) % 7)
	row = ((int(position[1]) - 1) % 7)
	if ((not col) and (not row)):
	    global_list.append(3)
	elif ((not col) or (not row)):
	    global_list.append(5)
	else:
	    global_list.append(8)
	return global_list