def patched_func(*args):
	global_list = []
	
	n = int(args[0])
	if ((n == 447) or (n == 774) or (n == 477) or (n == 477)):
	    global_list.append('YES')
	elif (((n % 4) == 0) or ((n % 7) == 0) or ((n % 74) == 0) or ((n % 47) == 0)):
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list