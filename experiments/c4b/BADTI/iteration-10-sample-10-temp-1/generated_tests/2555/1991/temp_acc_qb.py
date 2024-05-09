def patched_func(*args):
	global_list = []
	
	s = args[0]
	i = 0
	count = 0
	ans = False
	while (i < (len(s) - 1)):
	    if (s[i] == s[(i + 1)]):
	        count = (count + 1)
	        if (count == 6):
	            ans = True
	            break
	    else:
	        count = 0
	    i = (i + 1)
	if (ans == True):
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list