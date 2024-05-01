def original_func(*args):
	global_list = []
	
	s = args[0]
	df = 0
	for k in range(1, len(s)):
	    if (s[k] == s[(k - 1)]):
	        df += 1
	        if (df >= 7):
	            break
	    else:
	        df = 0
	if (df >= 7):
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list