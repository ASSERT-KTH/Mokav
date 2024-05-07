def patched_func(*args):
	global_list = []
	
	s = args[0]
	ans = 0
	val = True
	for a in s:
	    if ((a == '7') or (a == '4')):
	        ans = (ans + 1)
	s = str(ans)
	for a in s:
	    if ((a == '7') or (a == '4')):
	        ans = True
	    else:
	        ans = False
	        break
	if ans:
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list