def original_func(*args):
	global_list = []
	
	n = int(args[0])
	s = args[1]
	s1 = 0
	s2 = 0
	for i in range((n // 2)):
	    if (s[i] != s[((n - i) - 1)]):
	        import sys
	        global_list.append('NO')
	        sys.exit(0)
	global_list.append('YES')
	return global_list