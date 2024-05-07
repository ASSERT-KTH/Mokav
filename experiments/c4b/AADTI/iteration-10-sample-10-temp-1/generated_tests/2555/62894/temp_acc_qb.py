def patched_func(*args):
	global_list = []
	
	s = args[0]
	c = 1
	i = 1
	t = s[0]
	while ((c != 7) and (i < len(s))):
	    if (s[i] == t):
	        c += 1
	    else:
	        t = s[i]
	        c = 1
	    i += 1
	if (c == 7):
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list