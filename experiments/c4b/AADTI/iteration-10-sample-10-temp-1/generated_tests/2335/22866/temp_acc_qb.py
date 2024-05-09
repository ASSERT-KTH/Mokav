def patched_func(*args):
	global_list = []
	
	s = args[0]
	n = len(s)
	com = 'hello'
	j = 0
	if (n < 5):
	    global_list.append('NO')
	else:
	    for i in s:
	        if (com[j] == i):
	            j += 1
	        if (j > 4):
	            break
	    if (j > 4):
	        global_list.append('YES')
	    else:
	        global_list.append('NO')
	return global_list