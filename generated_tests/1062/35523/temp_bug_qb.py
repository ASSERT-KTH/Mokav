def original_func(*args):
	global_list = []
	
	t = args[0]
	t = t.replace('4', '')
	t = t.replace('7', '')
	if (len(t) < 1):
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list