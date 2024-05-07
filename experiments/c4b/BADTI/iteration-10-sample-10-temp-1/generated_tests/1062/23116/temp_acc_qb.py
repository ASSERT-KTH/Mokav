def patched_func(*args):
	global_list = []
	
	s = args[0]
	count = 0
	for i in range(len(s)):
	    if ((s[i] == '4') or (s[i] == '7')):
	        count += 1
	if ((count == 4) or (count == 7)):
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list