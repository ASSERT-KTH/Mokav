def original_func(*args):
	global_list = []
	
	a = args[0]
	f = 0
	for i in a:
	    if ((i == 'H') or (i == 'Q') or (i == '9') or (i == '+')):
	        f = 1
	        global_list.append('YES')
	        break
	if (f == 0):
	    global_list.append('NO')
	return global_list