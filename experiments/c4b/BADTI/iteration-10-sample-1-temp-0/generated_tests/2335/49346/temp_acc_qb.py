def patched_func(*args):
	global_list = []
	
	x = args[0]
	a = list()
	flag = 0
	for i in range(0, len(x)):
	    a.append(x[i])
	for i in range(0, len(a)):
	    if ((flag == 0) and (a[i] == 'h')):
	        flag = 1
	    elif ((flag == 1) and (a[i] == 'e')):
	        flag = 2
	    elif ((flag == 2) and (a[i] == 'l')):
	        flag = 3
	    elif ((flag == 3) and (a[i] == 'l')):
	        flag = 4
	    elif ((flag == 4) and (a[i] == 'o')):
	        flag = 5
	    elif (flag == 5):
	        break
	if (flag == 5):
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list