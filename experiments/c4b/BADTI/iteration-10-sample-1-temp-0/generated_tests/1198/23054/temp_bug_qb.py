def original_func(*args):
	global_list = []
	
	x = args[0]
	i = 0
	j = 1
	if ((x[i] == 'H') or (x[i] == 'Q')):
	    global_list.append('YES')
	elif (x.find('9') != (- 1)):
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list