def original_func(*args):
	global_list = []
	
	x = args[0]
	a = list()
	flag = 0
	for i in range(0, len(x)):
	    a.append(x[i])
	for i in range(0, len(a)):
	    if (((flag == 0) or (flag == 1)) and (a[i] == 'h')):
	        flag = 1
	    elif (((flag == 1) or (flag == 2)) and (a[i] == 'e')):
	        flag = 2
	    elif ((flag == 2) and (a[i] == 'l')):
	        flag = 3
	    elif (((flag == 3) or (flag == 4)) and (a[i] == 'l')):
	        flag = 4
	    elif (((flag == 4) or (flag == 5)) and (a[i] == 'o')):
	        flag = 5
	    elif (flag == 5):
	        break
	    elif (a[i] in ['h', 'e', 'l', 'o']):
	        flag = 0
	if (flag == 0):
	    global_list.append('NO')
	else:
	    global_list.append('YES')
	return global_list