def original_func(*args):
	global_list = []
	
	n = str(args[0])
	t = 0
	for k in range(len(n)):
	    if (n[k] == '0'):
	        t += 1
	j = 0
	for k in range(len(n)):
	    if (n[k] == '1'):
	        j += 1
	if ((t >= 7) or (j >= 7)):
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list