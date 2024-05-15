def original_func(*args):
	global_list = []
	
	a = args[0]
	arr = ['H', 'Q', '9', '+']
	narr = []
	for i in range(len(arr)):
	    if (arr[i] in a):
	        narr.append('YES')
	    else:
	        narr.append('NO')
	if ('YES' in narr):
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list