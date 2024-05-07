def original_func(*args):
	global_list = []
	
	p = str(args[0])
	a = False
	for i in range(len(p)):
	    if ((p[i] == 'H') or (p[i] == 'Q') or (p[i] == 9)):
	        a = True
	        break
	if (a == True):
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list