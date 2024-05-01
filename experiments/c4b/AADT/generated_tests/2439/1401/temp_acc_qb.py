def patched_func(*args):
	global_list = []
	
	S1 = args[0]
	S2 = args[1]
	ans1 = (int(S1) + int(S2))
	ans1 = str(ans1)
	ans11 = ''
	for a in ans1:
	    if (a != '0'):
	        ans11 += a
	new_S1 = ''
	for s in S1:
	    if (s != '0'):
	        new_S1 += s
	new_S2 = ''
	for s in S2:
	    if (s != '0'):
	        new_S2 += s
	ans2 = (int(new_S1) + int(new_S2))
	ans2 = str(ans2)
	if (ans11 == ans2):
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list