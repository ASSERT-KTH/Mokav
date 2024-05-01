def patched_func(*args):
	global_list = []
	
	n = str(args[0])
	l = len(n)
	p = 0
	for i in range(0, (l - 6)):
	    if (n[i] == n[(i + 1)] == n[(i + 2)] == n[(i + 3)] == n[(i + 4)] == n[(i + 5)] == n[(i + 6)]):
	        p = (p + 1)
	    else:
	        continue
	if (p >= 1):
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list