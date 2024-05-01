def patched_func(*args):
	global_list = []
	
	line = args[0]
	for i in line:
	    if ((i == 'H') or (i == 'Q') or (i == '9')):
	        global_list.append('YES')
	        break
	else:
	    global_list.append('NO')
	return global_list