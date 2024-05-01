def patched_func(*args):
	global_list = []
	
	s = args[0]
	(k, n, z) = (0, (len(s) // 2), len(s))
	for i in range(n):
	    if (s[i] != s[((z - i) - 1)]):
	        k += 1
	if (k == 1):
	    global_list.append('YES')
	elif ((k == 0) and ((z % 2) == 1)):
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list