def original_func(*args):
	global_list = []
	
	s = args[0]
	ans = True
	for a in s:
	    if ((a == '7') or (a == '4')):
	        continue
	    else:
	        ans = False
	        break
	if ans:
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list