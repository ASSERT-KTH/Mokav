def patched_func(*args):
	global_list = []
	
	n = int(args[0])
	a = (n // 4)
	b = (n % 4)
	if (((n % 2) == 0) and ((n // 4) >= 1)):
	    if (b == 2):
	        global_list.append(a)
	    else:
	        global_list.append((a - 1))
	else:
	    global_list.append(0)
	return global_list