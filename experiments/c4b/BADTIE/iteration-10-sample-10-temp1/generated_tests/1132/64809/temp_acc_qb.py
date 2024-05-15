def patched_func(*args):
	global_list = []
	
	n = int(args[0])
	if ((n % 4) and (n % 7) and (n % 47) and (n % 74) and (n % 447) and (n % 474) and (n % 477) and (n % 744) and (n % 747) and (n % 774)):
	    global_list.append('NO')
	else:
	    global_list.append('YES')
	return global_list