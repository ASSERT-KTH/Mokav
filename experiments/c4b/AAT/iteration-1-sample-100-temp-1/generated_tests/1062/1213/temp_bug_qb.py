def original_func(*args):
	global_list = []
	
	A = args[0]
	a = 0
	c = 0
	count = 0
	for i in A:
	    if ((i != '4') and (i != '7')):
	        a = 1
	    elif ((i == '4') or (i == '7')):
	        count = (count + 1)
	if ((A == '7') or (A == '4')):
	    global_list.append('NO')
	if ((a == 0) and (A != '7') and (A != '4')):
	    global_list.append('YES')
	elif (a == 1):
	    b = str(count)
	    for i in b:
	        if ((i != '4') and (i != '7')):
	            c = 1
	            break
	    if (c == 0):
	        global_list.append('YES')
	    else:
	        global_list.append('NO')
	return global_list