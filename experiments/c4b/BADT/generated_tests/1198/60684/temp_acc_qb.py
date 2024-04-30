def patched_func(*args):
	global_list = []
	
	A = args[0]
	k = 0
	while ((A[k] != 'H') and (A[k] != 'Q') and (A[k] != '9') and (k < (len(A) - 1))):
	    k += 1
	if (k < (len(A) - 1)):
	    global_list.append('YES')
	elif ((k == (len(A) - 1)) and ((A[k] == 'Q') or (A[k] == 'H') or (A[k] == '9'))):
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list