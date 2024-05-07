def original_func(*args):
	global_list = []
	
	x = args[0]
	x = list(x)
	if (('4' in x) and ('7' in x)):
	    for i in range(len(x)):
	        if ((x[i] != '7') and (x[i] != '4')):
	            x[i] = 's'
	    y = ''.join(x)
	    try:
	        if int(y):
	            global_list.append('YES')
	    except ValueError:
	        global_list.append('NO')
	else:
	    global_list.append('NO')
	return global_list