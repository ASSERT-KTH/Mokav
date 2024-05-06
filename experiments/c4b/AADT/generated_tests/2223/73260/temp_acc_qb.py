def patched_func(*args):
	global_list = []
	
	input_data = int(args[0])
	if (input_data != 2):
	    if ((input_data % 2) == 0):
	        global_list.append('YES')
	    else:
	        global_list.append('NO')
	else:
	    global_list.append('NO')
	return global_list