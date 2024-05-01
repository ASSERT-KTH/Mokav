def patched_func(*args):
	global_list = []
	
	a = args[0]
	arr = []
	if (len(a) >= 7):
	    for i in range((len(a) - 6)):
	        b = a[i:(i + 7)]
	        if (len(set(b)) == 1):
	            arr.append('YES')
	        else:
	            arr.append('NO')
	if ('YES' in arr):
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list