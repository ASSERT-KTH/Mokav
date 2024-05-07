def patched_func(*args):
	global_list = []
	
	a = '6842'
	n = int(args[0])
	if (n == 0):
	    global_list.append(1)
	else:
	    n %= 4
	    global_list.append(a[n])
	return global_list