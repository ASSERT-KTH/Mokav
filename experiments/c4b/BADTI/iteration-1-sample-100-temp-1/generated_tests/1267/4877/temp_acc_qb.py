def patched_func(*args):
	global_list = []
	
	args[0]
	s = args[1]
	for c in s:
	    if ((c != '4') and (c != '7')):
	        global_list.append('NO')
	        break
	else:
	    if (sum([int(i) for i in s[:(len(s) // 2)]]) == sum([int(i) for i in s[(- 1):((len(s) // 2) - 1):(- 1)]])):
	        global_list.append('YES')
	    else:
	        global_list.append('NO')
	return global_list