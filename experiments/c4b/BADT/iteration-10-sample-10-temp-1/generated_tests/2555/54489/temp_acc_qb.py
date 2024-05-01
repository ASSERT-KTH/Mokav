def patched_func(*args):
	global_list = []
	
	count = 0
	i = 0
	arr = []
	k = args[0]
	for a in k:
	    arr.append(int(a))
	while (i < (len(arr) - 1)):
	    i += 1
	    if (arr[(i - 1)] == arr[i]):
	        count += 1
	    if (arr[(i - 1)] != arr[i]):
	        count = 0
	    if (count >= 6):
	        global_list.append('YES')
	        break
	if (count < 6):
	    global_list.append('NO')
	return global_list