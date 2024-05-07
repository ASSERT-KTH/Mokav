def original_func(*args):
	global_list = []
	
	n = str(args[0].strip())
	if ((len(n) == 4) or (len(n) == 7)):
	    for i in n:
	        if ((i == '7') or (i == '4')):
	            fl = True
	        else:
	            fl = False
	            break
	else:
	    fl = False
	if (fl == True):
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list