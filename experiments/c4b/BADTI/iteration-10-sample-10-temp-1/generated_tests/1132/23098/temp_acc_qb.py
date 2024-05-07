def patched_func(*args):
	global_list = []
	
	n = int(args[0])
	if (((n % 4) == 0) or ((n % 7) == 0) or ((n % 47) == 0) or ((n % 74) == 0) or ((n % 444) == 0) or ((n % 447) == 0) or ((n % 477) == 0) or ((n % 744) == 0) or ((n % 774) == 0) or ((n % 777) == 0)):
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list