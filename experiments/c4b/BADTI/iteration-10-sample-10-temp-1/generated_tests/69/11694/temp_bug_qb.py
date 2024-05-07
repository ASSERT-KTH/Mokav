def original_func(*args):
	global_list = []
	
	n = int(args[0])
	if (n == 3):
	    global_list.append('1')
	else:
	    cnt = (((n - 1) * 2) + 1)
	    global_list.append(cnt)
	return global_list