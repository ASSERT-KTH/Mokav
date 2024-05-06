def original_func(*args):
	global_list = []
	
	num = args[0]
	bol = 'true'
	if (((int(num) % 4) == 0) or ((int(num) % 7) == 0)):
	    global_list.append('YES')
	else:
	    for i in range(0, len(num)):
	        if ((num[i] != '4') and (num[i] != '7')):
	            bol = 'false'
	            break
	    if (bol == 'true'):
	        global_list.append('YES')
	    else:
	        global_list.append('NO')
	return global_list