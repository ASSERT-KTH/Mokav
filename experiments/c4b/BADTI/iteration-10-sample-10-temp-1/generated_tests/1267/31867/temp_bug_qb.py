def original_func(*args):
	global_list = []
	
	n = int(args[0])
	num = args[1]
	flag = 0
	for i in num:
	    if ((i < '4') or ('4' < i < '7') or (i > '7')):
	        global_list.append('NO')
	        flag = 1
	        break
	if (flag == 0):
	    if (sum(map(int, num[:(n // 2)])) == sum(map(int, num[(n // 2):]))):
	        global_list.append('YES')
	return global_list