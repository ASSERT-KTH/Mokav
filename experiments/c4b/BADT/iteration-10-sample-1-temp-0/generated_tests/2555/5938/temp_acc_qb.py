def patched_func(*args):
	global_list = []
	
	s = args[0]
	res = 0
	for i in range((len(s) - 1)):
	    if (s[i] == s[(i + 1)]):
	        res += 1
	    else:
	        res = 0
	    if (res >= 6):
	        global_list.append('YES')
	        break
	else:
	    global_list.append('NO')
	return global_list