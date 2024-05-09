def patched_func(*args):
	global_list = []
	
	a = args[0]
	b = a.split()
	if (((int(b[0]) % 2) == 1) and ((int(b[1]) % 2) == 1)):
	    global_list.append(int((((int(b[0]) * int(b[1])) - 1) / 2)))
	else:
	    global_list.append(int(((int(b[0]) * int(b[1])) / 2)))
	return global_list