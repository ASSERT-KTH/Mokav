def patched_func(*args):
	global_list = []
	
	x = args[0]
	test = '0'
	i = 0
	y = 0
	while (i < len(x)):
	    if (test == x[i]):
	        y += 1
	        if (y == 7):
	            global_list.append('YES')
	            break
	    else:
	        y = 1
	        test = x[i]
	    i += 1
	else:
	    global_list.append('NO')
	return global_list