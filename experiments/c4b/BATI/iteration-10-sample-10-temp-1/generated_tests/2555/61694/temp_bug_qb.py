def original_func(*args):
	global_list = []
	
	n = int(args[0])
	temp = str(n)
	count = 0
	flag = 0
	for i in range((len(temp) - 1)):
	    if (temp[i] == temp[(i + 1)]):
	        count += 1
	        if (count >= 6):
	            flag = 1
	            global_list.append('YES')
	            break
	    if (temp[i] != temp[(i + 1)]):
	        count = 0
	if (flag == 0):
	    global_list.append('NO')
	return global_list