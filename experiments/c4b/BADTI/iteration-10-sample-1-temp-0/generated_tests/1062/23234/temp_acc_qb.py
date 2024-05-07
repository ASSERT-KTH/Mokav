def patched_func(*args):
	global_list = []
	
	n = args[0]
	if (((n.count('4') + n.count('7')) == 7) or ((n.count('4') + n.count('7')) == 4)):
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list