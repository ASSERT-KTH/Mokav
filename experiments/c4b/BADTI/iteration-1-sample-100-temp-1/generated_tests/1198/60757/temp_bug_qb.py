def original_func(*args):
	global_list = []
	
	flag = 0
	str = args[0]
	a = ['H', 'Q', '9', '+']
	for i in str:
	    if (i in a):
	        flag = 1
	if (flag == 1):
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list