def patched_func(*args):
	global_list = []
	
	a = args[0]
	x = list()
	flag = 0
	for i in range(0, len(a)):
	    if ((a[i] == '4') or (a[i] == '7')):
	        flag += 1
	if ((flag == 4) or (flag == 7)):
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list