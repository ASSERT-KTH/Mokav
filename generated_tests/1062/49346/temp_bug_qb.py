def original_func(*args):
	global_list = []
	
	a = args[0]
	x = list()
	flag = 0
	for i in range(0, len(a)):
	    x.append(a[i])
	if (('0' in x) or ('1' in x) or ('2' in x) or ('3' in x) or ('5' in x) or ('6' in x) or ('8' in x) or ('9' in x)):
	    flag = 1
	if (flag == 0):
	    global_list.append('YES')
	elif (flag == 1):
	    global_list.append('NO')
	return global_list