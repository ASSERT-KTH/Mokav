def original_func(*args):
	global_list = []
	
	(n, m) = map(int, args[0].split())
	if ((n == 2) and (m == 3)):
	    global_list.append('YES')
	elif ((n == 2) and (m != 3)):
	    global_list.append('NO')
	else:
	    k = (n + 2)
	    i = 3
	    while (i <= (m ** 0.5)):
	        while ((k % i) == 0):
	            k += 2
	        i += 2
	    if (k == m):
	        global_list.append('YES')
	    else:
	        global_list.append('NO')
	return global_list