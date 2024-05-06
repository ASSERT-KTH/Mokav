def original_func(*args):
	global_list = []
	
	s = args[0]
	ans = 0
	c = 0
	for i in s:
	    c += 1
	    if ((i == 'A') or (i == 'E') or (i == 'I') or (i == 'O') or (i == 'U') or (i == 'Y')):
	        if (c > ans):
	            ans = c
	        c = 0
	if (ans == 0):
	    global_list.append((c + 1))
	else:
	    global_list.append(ans)
	return global_list