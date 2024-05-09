def patched_func(*args):
	global_list = []
	
	a = args[0]
	a = list(a)
	k = 0
	for x in a:
	    if ((k == 0) and (x == 'h')):
	        k = (k + 1)
	    elif ((k == 1) and (x == 'e')):
	        k = (k + 1)
	    elif ((k == 2) and (x == 'l')):
	        k = (k + 1)
	    elif ((k == 3) and (x == 'l')):
	        k = (k + 1)
	    elif ((k == 4) and (x == 'o')):
	        k = (k + 1)
	if (k == 5):
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list