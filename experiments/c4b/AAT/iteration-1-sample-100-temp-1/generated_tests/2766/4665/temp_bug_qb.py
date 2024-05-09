def original_func(*args):
	global_list = []
	
	s = args[0]
	length = len(s)
	miss = 0
	for i in range(0, (length // 2)):
	    if (s[i] != s[((length - 1) - i)]):
	        miss += 1
	if (miss == 1):
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list