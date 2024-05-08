def original_func(*args):
	global_list = []
	
	y = int(args[0])
	while (y < 9000):
	    y += 1
	    s = str(y)
	    if ((s[0] != s[1]) and (s[0] != s[2]) and (s[0] != s[3]) and (s[1] != s[2]) and (s[1] != s[3]) and (s[2] != s[3])):
	        global_list.append(s)
	        break
	return global_list