def original_func(*args):
	global_list = []
	
	n = int(args[0])
	flag = 0
	if (((n % 4) == 0) or ((n % 7) == 0)):
	    global_list.append('YES')
	else:
	    string = str(n)
	    for i in string:
	        if ((i == '4') or (i == '7')):
	            continue
	        else:
	            global_list.append('NO')
	            flag = 1
	            break
	    if (flag == 0):
	        global_list.append('YES')
	return global_list