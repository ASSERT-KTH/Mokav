def patched_func(*args):
	global_list = []
	
	temp = args[0]
	count = 0
	flag = 0
	for i in range((len(temp) - 1)):
	    if (temp[i] == temp[(i + 1)]):
	        count += 1
	        if (count >= 6):
	            global_list.append('YES')
	            flag = 1
	            break
	    if (temp[i] != temp[(i + 1)]):
	        count = 0
	if (flag == 0):
	    global_list.append('NO')
	return global_list