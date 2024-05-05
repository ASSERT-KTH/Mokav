def original_func(*args):
	global_list = []
	
	A = args[0]
	a = 0
	for i in A:
	    if ((i == 'H') or (i == 'Q') or (i == '9') or (i == '+')):
	        global_list.append('YES')
	        a = 1
	        break
	if (a == 0):
	    global_list.append('NO')
	return global_list