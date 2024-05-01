def patched_func(*args):
	global_list = []
	
	(n, m) = list(map(int, args[0].split()))
	c = (n + 1)
	while (c <= m):
	    for i in range((c - 1), 1, (- 1)):
	        if ((c % i) == 0):
	            break
	    else:
	        if (c < m):
	            global_list.append('NO')
	        elif (c == m):
	            global_list.append('YES')
	        exit()
	    c += 1
	else:
	    global_list.append('NO')
	return global_list