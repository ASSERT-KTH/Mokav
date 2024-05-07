def original_func(*args):
	global_list = []
	
	ip = args[0].strip()
	old_key = None
	count = 0
	flag = 0
	for c in ip:
	    if (old_key == None):
	        old_key = c
	        count = 1
	    elif (old_key == c):
	        count += 1
	    else:
	        if (count >= 7):
	            flag = 1
	            break
	        old_key = c
	        count = 1
	if (flag == 0):
	    global_list.append('NO')
	elif (flag == 1):
	    global_list.append('YES')
	return global_list