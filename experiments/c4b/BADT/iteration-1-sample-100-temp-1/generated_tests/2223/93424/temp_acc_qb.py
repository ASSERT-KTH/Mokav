def patched_func(*args):
	global_list = []
	
	numb = int(args[0])
	if (((numb % 2) == 0) and (numb != 2) and (numb != 0)):
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list