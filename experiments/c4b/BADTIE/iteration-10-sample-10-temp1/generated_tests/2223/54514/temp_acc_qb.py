def patched_func(*args):
	global_list = []
	
	number = int(args[0])
	if (number == 2):
	    global_list.append('NO')
	elif ((number % 2) == 0):
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list