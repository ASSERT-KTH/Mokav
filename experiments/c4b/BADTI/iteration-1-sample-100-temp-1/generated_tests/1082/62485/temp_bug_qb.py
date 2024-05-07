def original_func(*args):
	global_list = []
	
	K = int(args[0])
	L = int(args[1])
	if ((L % K) != 0):
	    global_list.append('NO')
	else:
	    importance = 0
	    while (L > 1):
	        L = (L // K)
	        importance += 1
	    if (L == 1):
	        global_list.append('YES')
	        global_list.append((importance - 1))
	    else:
	        global_list.append('NO')
	return global_list