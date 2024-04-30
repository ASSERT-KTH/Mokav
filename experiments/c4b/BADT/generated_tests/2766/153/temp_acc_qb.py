def patched_func(*args):
	global_list = []
	
	s = args[0]
	n = len(s)
	l = 0
	for i in range(n):
	    if (s[i] != s[((n - 1) - i)]):
	        l += 1
	if ((l == 2) or ((l == 0) and ((n % 2) == 1))):
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list