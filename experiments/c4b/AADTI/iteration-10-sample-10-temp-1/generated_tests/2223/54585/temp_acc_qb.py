def patched_func(*args):
	global_list = []
	
	kilo = args[0]
	kgs = int(kilo)
	if (((kgs % 2) == 0) and (kgs != 2)):
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list