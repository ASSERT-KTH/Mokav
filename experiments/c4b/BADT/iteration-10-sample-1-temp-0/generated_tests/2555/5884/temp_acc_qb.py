def patched_func(*args):
	global_list = []
	
	st = args[0]
	length = len(st)
	count = 0
	if (length < 7):
	    global_list.append('NO')
	else:
	    for i in range(length):
	        if (i == 0):
	            continue
	        if (st[i] == st[(i - 1)]):
	            count = (count + 1)
	            if (count >= 6):
	                global_list.append('YES')
	                break
	        else:
	            if (count >= 6):
	                global_list.append('YES')
	                break
	            count = 0
	    if (count < 6):
	        global_list.append('NO')
	return global_list