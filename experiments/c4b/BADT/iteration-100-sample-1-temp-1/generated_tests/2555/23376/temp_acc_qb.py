def patched_func(*args):
	global_list = []
	
	s = args[0]
	s += '2'
	i = 0
	sum = 1
	while ((i < (len(s) - 1)) and (sum < 7)):
	    if (s[i] == s[(i + 1)]):
	        sum += 1
	    else:
	        sum = 1
	    i += 1
	if (sum >= 7):
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list