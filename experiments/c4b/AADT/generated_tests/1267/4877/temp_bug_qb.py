def original_func(*args):
	global_list = []
	
	args[0]
	s = args[1]
	for c in s:
	    if ((c != '4') and (c != '7')):
	        global_list.append('NO')
	        break
	else:
	    if (s[:(len(s) // 2)] == s[(- 1):((len(s) // 2) - 1):(- 1)]):
	        global_list.append('YES')
	    else:
	        global_list.append('NO')
	return global_list