def patched_func(*args):
	global_list = []
	
	(m, n) = map(int, args[0].split())
	(k, p) = map(int, args[1].split())
	l = 0
	if (((m - p) < 2) and ((p - m) < ((m + 1) * 2))):
	    l += 1
	if (((n - k) < 2) and ((k - n) < ((n + 1) * 2))):
	    l += 1
	if (l < 1):
	    global_list.append('NO')
	else:
	    global_list.append('YES')
	return global_list