def original_func(*args):
	global_list = []
	
	n = int(args[0])
	s = args[1]
	if ((s.count('7') + s.count('4')) != len(s)):
	    global_list.append('no')
	else:
	    s1 = 0
	    s2 = 0
	    for i in s[:(n // 2)]:
	        s1 += int(i)
	    for i in s[(n // 2):]:
	        s2 += int(i)
	    if (s1 == s2):
	        global_list.append('yes')
	    else:
	        global_list.append('no')
	return global_list