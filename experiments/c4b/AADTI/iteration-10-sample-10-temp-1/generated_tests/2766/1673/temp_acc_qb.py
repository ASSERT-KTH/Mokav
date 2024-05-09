def patched_func(*args):
	global_list = []
	
	N = str(args[0].split()[0])
	P = N[(- 1)::(- 1)]
	k = 0
	for i in range(0, len(N)):
	    if (N[i] != P[i]):
	        k += 1
	if (k == 0):
	    if ((len(N) % 2) == 0):
	        global_list.append('NO')
	    else:
	        global_list.append('YES')
	elif ((k - 1) == 1):
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list