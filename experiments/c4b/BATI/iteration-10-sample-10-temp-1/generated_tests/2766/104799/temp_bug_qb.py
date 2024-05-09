def original_func(*args):
	global_list = []
	
	s = args[0]
	l = len(s)
	new = s[::(- 1)]
	i = 0
	count = 0
	while (i < l):
	    if (new[i] != s[i]):
	        count = (count + 1)
	    i = (i + 1)
	if (count == 1):
	    global_list.append('Yes')
	elif (count > 1):
	    global_list.append('No')
	elif ((l % 2) == 0):
	    global_list.append('NO')
	else:
	    global_list.append('Yes')
	return global_list