def original_func(*args):
	global_list = []
	
	num = int(args[0])
	if (((num % 4) == 0) or ((num % 7) == 0) or ((num % 47) == 0)):
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list