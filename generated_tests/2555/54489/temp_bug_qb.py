def original_func(*args):
	global_list = []
	
	count = 0
	i = 1
	arr = []
	k = args[0]
	for j in k:
	    arr.append(int(j))
	while (i <= (len(arr) - 1)):
	    if (arr[i] == arr[(i - 1)]):
	        count += 1
	    else:
	        count -= 1
	    if (count < 0):
	        count = 0
	    if (count >= 6):
	        global_list.append('YES')
	        break
	    i += 1
	if (count < 6):
	    global_list.append('NO')
	return global_list