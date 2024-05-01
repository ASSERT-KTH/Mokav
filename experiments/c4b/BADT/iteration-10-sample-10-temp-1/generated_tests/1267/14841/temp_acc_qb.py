def patched_func(*args):
	global_list = []
	
	n = int(args[0])
	s = args[1]
	s1 = 0
	s2 = 0
	for i in range((n // 2)):
	    if ((s[i] != '7') and (s[i] != '4')):
	        import sys
	        global_list.append('NO')
	        sys.exit(0)
	    s1 += (ord(s[i]) - 48)
	for i in range((n // 2), n):
	    if ((s[i] != '7') and (s[i] != '4')):
	        import sys
	        global_list.append('NO')
	        sys.exit(0)
	    s2 += (ord(s[i]) - 48)
	if (s1 == s2):
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list