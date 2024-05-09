def patched_func(*args):
	global_list = []
	
	(n, k) = [int(i) for i in args[0].split()]
	if (abs((n - k)) <= 1):
	    if (n == k == 0):
	        global_list.append('NO')
	    else:
	        global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list