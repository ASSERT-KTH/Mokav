def original_func(*args):
	global_list = []
	
	p = args[0]
	i = 0
	while (i < len(p)):
	    if ((p[i] == 'H') or (p[i] == 'Q') or (p[i] == '9') or (p[i] == '+')):
	        global_list.append('YES')
	        break
	    i += 1
	else:
	    global_list.append('NO')
	return global_list