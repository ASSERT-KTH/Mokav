def original_func(*args):
	global_list = []
	
	s = args[0]
	(k, n, z) = (0, (len(s) // 2), len(s))
	for i in range(n):
	    if (s[i] != s[((z - i) - 1)]):
	        k += 1
	if (k != 1):
	    global_list.append('NO')
	else:
	    global_list.append('YES')
	return global_list