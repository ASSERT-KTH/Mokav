def patched_func(*args):
	global_list = []
	
	x = int(args[0])
	for i in range((x + 1), 9500):
	    s = str(i)
	    if ((s[0] != s[1]) and (s[2] != s[1]) and (s[2] != s[0]) and (s[3] != s[2]) and (s[1] != s[3]) and (s[3] != s[0])):
	        s1 = int(s)
	        global_list.append(s1)
	        break
	    i = (i + 1)
	return global_list