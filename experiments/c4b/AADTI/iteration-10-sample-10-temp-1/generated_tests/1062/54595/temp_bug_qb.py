def original_func(*args):
	global_list = []
	
	s = args[0]
	if ((len(s) != 4) and (len(s) != 7)):
	    global_list.append('NO')
	    exit()
	for i in range(len(s)):
	    if ((s[i] != '4') and (s[i] != '7')):
	        global_list.append('NO')
	        exit()
	global_list.append('YES')
	return global_list