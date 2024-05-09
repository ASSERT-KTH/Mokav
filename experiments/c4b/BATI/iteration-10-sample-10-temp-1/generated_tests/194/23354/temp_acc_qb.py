def patched_func(*args):
	global_list = []
	
	x = int(args[0])
	if (x >= 6):
	    if ((x / 5) != (x // 5)):
	        i = ((x // 5) + 1)
	    else:
	        i = (x // 5)
	    global_list.append(str(i))
	else:
	    global_list.append('1')
	return global_list