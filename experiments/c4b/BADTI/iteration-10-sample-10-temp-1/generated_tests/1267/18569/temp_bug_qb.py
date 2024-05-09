def original_func(*args):
	global_list = []
	
	n = int(args[0])
	num = [int(x) for x in args[1]]
	ok = 1
	for i in num:
	    if ((i == 4) or (i == 7)):
	        pass
	    else:
	        ok = 0
	s1 = 0
	s2 = 0
	for i in range(0, (n // 2)):
	    global_list.append(i)
	    s1 += num[i]
	for i in range((n // 2), n):
	    s2 += num[i]
	if (s1 != s2):
	    ok = 0
	if (ok == 1):
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list