def patched_func(*args):
	global_list = []
	
	(p, n) = args[0].split()
	p = int(p)
	n = int(n)
	if ((p == 0) and (n == 0)):
	    global_list.append('NO')
	elif ((p == n) or ((n - p) == 1) or ((p - n) == 1)):
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list