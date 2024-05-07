def patched_func(*args):
	global_list = []
	
	l = list(args[0])
	if (((l.count('4') + l.count('7')) == 4) or ((l.count('4') + l.count('7')) == 7)):
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list