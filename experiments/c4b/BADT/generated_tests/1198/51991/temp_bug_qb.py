def original_func(*args):
	global_list = []
	
	p = str(args[0])
	for i in range(0, len(p)):
	    if ((p[i] == 'H') or (p[i] == 'Q') or (p[i] == '9') or (p[i] == '+')):
	        global_list.append('YES')
	        break
	else:
	    global_list.append('NO')
	return global_list