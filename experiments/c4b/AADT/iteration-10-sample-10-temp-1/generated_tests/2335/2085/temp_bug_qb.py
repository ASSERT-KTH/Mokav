def original_func(*args):
	global_list = []
	
	a = args[0]
	m = 0
	s = 0
	for r in range(0, len(a)):
	    if ((a[r] == 'h') and (m == 0) and (r > s)):
	        m += 1
	        s = r
	    elif ((a[r] == 'e') and (m == 1) and (r > s)):
	        m += 2
	        s = r
	    elif ((a[r] == 'l') and (m == 3) and (r > s)):
	        m += 3
	        s = r
	    elif ((a[r] == 'l') and (m == 6) and (r > s)):
	        m += 4
	        s = r
	    elif ((a[r] == 'o') and (m == 10) and (r > s)):
	        m += 5
	if (m == 15):
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list