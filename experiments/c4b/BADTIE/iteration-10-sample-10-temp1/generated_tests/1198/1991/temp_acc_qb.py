def patched_func(*args):
	global_list = []
	
	s = args[0]
	ans = False
	for a in s:
	    if ((a == 'H') or (a == 'Q') or (a == '9')):
	        global_list.append('YES')
	        ans = True
	        break
	if (not ans):
	    global_list.append('NO')
	return global_list