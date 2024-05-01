def patched_func(*args):
	global_list = []
	
	n = args[0]
	k = len(n)
	m = 0
	j = 0
	for i in range((k - 1)):
	    if (n[i] == n[(i + 1)]):
	        j = (j + 1)
	        if (j == 6):
	            global_list.append('YES')
	            break
	    else:
	        j = 0
	if (j < 6):
	    global_list.append('NO')
	return global_list