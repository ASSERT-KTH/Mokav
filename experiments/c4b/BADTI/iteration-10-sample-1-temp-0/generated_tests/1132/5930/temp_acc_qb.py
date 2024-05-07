def patched_func(*args):
	global_list = []
	
	n = int(args[0])
	s = list(str(n))
	c = 0
	for i in range(len(s)):
	    if ((s[i] == '4') or (s[i] == '7')):
	        c = (c + 1)
	if (((n % 4) == 0) or ((n % 7) == 0) or ((n % 47) == 0)):
	    global_list.append('YES')
	elif (c == len(s)):
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list