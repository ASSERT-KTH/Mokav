def patched_func(*args):
	global_list = []
	
	s = args[0]
	tmp = 0
	for i in range(len(s)):
	    if ((s[i] == '4') or (s[i] == '7')):
	        tmp += 1
	if ((tmp == 4) or (tmp == 7)):
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list